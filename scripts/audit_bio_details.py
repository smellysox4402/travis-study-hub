#!/usr/bin/env python3
"""Detail audit: check each new bio page contains the specific exam-mandated
examples/names/mechanisms the syllabus requires. Missing = detail gap."""
import re, os

BASE = r"C:/Users/ASUS/Desktop/Hermes_Workspace/study-hub/topics/bio"

# topic -> list of (required detail substring, note) — from the syllabus statements
DETAIL = {
 "a1.1-water": [
   ("hydrogen bond", "A1.1.2 H-bonds"), ("δ−","delta- notation"), ("δ+","delta+"),
   ("cohesion","A1.1.3"), ("surface tension","A1.1.3"), ("xylem","A1.1.3"),
   ("adhesion","A1.1.4"), ("capillary action","A1.1.4"), ("soil","A1.1.4"),
   ("hydrophilic","A1.1.5"), ("hydrophobic","A1.1.5"),
   ("buoyancy","A1.1.6"), ("viscosity","A1.1.6"), ("thermal conductivity","A1.1.6"),
   ("specific heat capacity","A1.1.6"), ("black-throated loon","A1.1.6 Gavia arctica"), ("ringed seal","A1.1.6 Pusa hispida"),
   ("asteroid","A1.1.7"), ("Gravity","A1.1.7 retention"), ("Goldilocks","A1.1.8"),
 ],
 "a1.2-nucleic-acids": [
   ("phosphate","nucleotide"), ("pentose","sugar"), ("nitrogenous base","base"),
   ("δ−","polarity"), ("adenine","base"), ("thymine","base"), ("guanine","base"), ("cytosine","base"), ("uracil","RNA base"),
   ("purine","AHL"), ("pyrimidine","AHL"), ("deoxyribose","DNA sugar"), ("ribose","RNA sugar"),
   ("antiparallel","A1.2.6"), ("hydrogen bond","base pairing"), ("double helix","A1.2.6"),
   ("5′","directionality AHL 5'"), ("3′","directionality AHL 3'"),
   ("nucleosome","AHL A1.2.13"), ("eight","histones"), ("H1","linker histone"),
   ("Hershey","AHL A1.2.14"), ("radioisotop","AHL"), ("32P","DNA label"), ("35S","protein label"),
   ("Chargaff","AHL A1.2.15"), ("tetranucleotide","AHL"), ("falsif","AHL"),
 ],
 "a2.1-origins-of-cells": [
   ("no free oxygen","A2.1.1"), ("ozone","A2.1.1"), ("carbon dioxide","A2.1.1"), ("methane","A2.1.1"),
   ("cell","smallest unit"), ("virus","non-living"), ("catalysis","A2.1.3"), ("self-replication","A2.1.3"),
   ("self-assembly","A2.1.3"), ("compartmentali","A2.1.3"), ("Miller","A2.1.4"), ("Urey","A2.1.4"), ("spark","A2.1.4"),
   ("amino acid","A2.1.4 result"), ("fatty acid","A2.1.5 vesicle"), ("bilayer","A2.1.5"), ("vesicle","A2.1.5"),
   ("RNA","A2.1.6"), ("ribozyme","A2.1.6"), ("peptide bond","A2.1.6 ribosome RNA"),
   ("universal genetic code","A2.1.7 LUCA"), ("common ancestor","A2.1.7"),
   ("hydrothermal vent","A2.1.9"),
 ],
 "a2.2-cell-structure": [
   ("eyepiece graticule","A2.2.2"), ("magnification","A2.2.2"), ("scale bar","A2.2.2"),
   ("electron micro","A2.2.3"), ("freeze fracture","A2.2.3"), ("cryogenic","A2.2.3"), ("fluorescent","A2.2.3"), ("immunofluoresc","A2.2.3"),
   ("plasma membrane","common feature"), ("DNA","genetic material"), ("cytoplasm","common"),
   ("70S","prokaryote"), ("naked DNA","loop"), ("cell wall","prokaryote"), ("Peptidoglycan","cell wall type"), ("Bacillus","example"), ("Staphylococcus","example"),
   ("80S","eukaryote"), ("histone","nucleus"), ("nucleus","eukaryote"), ("Golgi","organelle"),
   ("cytoskeleton","eukaryote"), ("microtubule","cytoskeleton"), ("microfilament","cytoskeleton"),
   ("homeostasis","life process"), ("excretion","life process"),
   ("cellulose","plant wall"), ("chitin","fungal wall"), ("sap vacuole","plant"), ("chloroplast","plant"),
   ("aseptate","atypical hyphae"), ("multinucleate","muscle"), ("sieve tube","no nucleus"),
   ("endosymbiosis","AHL A2.2.12"), ("70S ribosome","endosymbiosis evidence"), ("circular DNA","endosymbiosis"),
   ("differentiat","AHL A2.2.13"), ("gene expression","AHL"), ("multicellular","AHL A2.2.14"),
 ],
 "a2.3-viruses": [
   ("capsid","A2.3.1"), ("nucleic acid","A2.3.1"), ("no cytoplasm","A2.3.1"), ("enzyme","few enzymes"),
   ("DNA or RNA","A2.3.2"), ("single- or double-","A2.3.2"), ("envelope","A2.3.2"),
   ("bacteriophage lambda","A2.3.3"), ("lytic","A2.3.3"), ("lysogenic","A2.3.4"), ("prophage","A2.3.4"),
   ("obligate","A2.3.5"), ("influenza","A2.3.6"), ("HIV","A2.3.6"), ("reverse transcriptase","A2.3.6 HIV"),
   ("combination therapy","A2.3.6 treatment"), ("vaccine","A2.3.6"),
 ],
 "a3.2-classification-cladistics": [
   ("kingdom","hierarchy"), ("phylum","hierarchy"), ("species","hierarchy"),
   ("clade","A3.2.4"), ("base sequence","A3.2.4"), ("amino acid sequence","A3.2.4"),
   ("molecular clock","A3.2.5"), ("cladogram","A3.2.6"), ("root","A3.2.7"), ("node","A3.2.7"), ("terminal branch","A3.2.7"),
   ("domain","A3.2.9"), ("Bacteria","domains"), ("Archaea","domains"), ("Eukarya","domains"), ("rRNA","A3.2.9"), ("1977","A3.2.9"),
   ("monophyletic","A3.2.3"),
 ],
 "a4.1-evolution-speciation": [
   ("heritable characteristics","A4.1.1"), ("population","A4.1.1"), ("Lamarck","A4.1.1"),
   ("base sequence","A4.1.2"), ("selective breeding","A4.1.3"),
   ("homologous","A4.1.4"), ("pentadactyl","A4.1.4"),
   ("convergent","A4.1.5"), ("analogous","A4.1.5"), ("bird","insect wing"),
   ("speciation","A4.1.6"), ("reproductive isolation","A4.1.7"), ("differential selection","A4.1.7"),
   ("geograph","A4.1.7"), ("bonobo","A4.1.7 chimp"), ("chimpanzee","A4.1.7"),
   ("allopatric","AHL A4.1.8"), ("sympatric","AHL A4.1.8"), ("adaptive radiation","AHL A4.1.9"),
   ("hybridiz","AHL A4.1.10"), ("sterile","AHL A4.1.10"), ("courtship","AHL A4.1.10"),
   ("polyploid","AHL A4.1.11"), ("Persicaria","AHL A4.1.11"),
 ],
 "a4.2-conservation-biodiversity": [
   ("ecosystem diversity","A4.2.1"), ("species diversity","A4.2.1"), ("genetic diversity","A4.2.1"),
   ("millions","A4.2.2"), ("sixth","mass extinction"), ("anthropogenic","A4.2.3"),
   ("dipterocarp","A4.2.4"), ("IPBES","A4.2.5"), ("population growth","A4.2.6"), ("over-exploitation","A4.2.6"), ("urbanization","A4.2.6"), ("deforestation","A4.2.6"),
   ("in situ","A4.2.7"), ("ex situ","A4.2.7"), ("seed bank","A4.2.7"),
   ("EDGE","A4.2.8"), ("globally endangered","A4.2.8"), ("evolutionarily distinct","A4.2.8"),
 ],
 "b1.1-carbohydrates-lipids": [
   ("four","bonds"), ("covalent","B1.1.1"), ("chain","B1.1.1"), ("ring","B1.1.1"),
   ("condensation","B1.1.2"), ("hydrolysis","B1.1.3"),
   ("pentose","B1.1.4"), ("hexose","B1.1.4"), ("glucose","B1.1.4"),
   ("starch","B1.1.5"), ("glycogen","B1.1.5"), ("insolub","B1.1.5"),
   ("β-glucose","B1.1.6"), ("cellulose","B1.1.6"),
   ("glycoprotein","B1.1.7"), ("ABO","B1.1.7"),
   ("non-polar","B1.1.8"), ("wax","B1.1.8"), ("steroid","B1.1.8"),
   ("triglyceride","B1.1.9"), ("phospholipid","B1.1.9"), ("glycerol","B1.1.9"),
   ("saturated","B1.1.10"), ("monounsaturated","B1.1.10"), ("polyunsaturated","B1.1.10"), ("double bond","B1.1.10"),
   ("adipose","B1.1.11"), ("insulation","B1.1.11"),
   ("amphipathic","B1.1.12"),
   ("oestradiol","B1.1.13"), ("testosterone","B1.1.13"),
 ],
 "b1.2-proteins": [
   ("alpha carbon","B1.2.1"), ("amine","B1.2.1"), ("carboxyl","B1.2.1"), ("R-group","B1.2.1"),
   ("dipeptide","B1.2.2"), ("peptide bond","B1.2.2"), ("+ water","B1.2.2 word eq"),
   ("Essential","B1.2.3"), ("non-essential","B1.2.3"), ("vegan","B1.2.3"),
   ("20","amino acids"), ("denaturat","B1.2.5"),
   ("hydrophilic","R-groups"), ("charged","R-groups"), ("acidic","basic R"), ("basic","R"),
   ("primary","structure"), ("conformation","B1.2.7"),
   ("alpha helic","B1.2.8"), ("beta-pleated","B1.2.8"), ("hydrogen bond","secondary"),
   ("ionic bond","tertiary"), ("disulfide","tertiary"), ("hydrophobic interaction","tertiary"),
   ("globular","soluble core"), ("core","hydrophobic cluster"), ("integral membrane","B1.2.10"),
   ("quaternary","B1.2.11"), ("insulin","non-conjugated"), ("collagen","non-conjugated"), ("haemoglobin","conjugated"),
   ("globular","B1.2.12"), ("fibrous","B1.2.12"),
 ],
 "b2.1-membranes": [
   ("bilayer","B2.1.1"), ("amphipathic","B2.1.1"), ("fluidity","fluid mosaic"),
   ("impermeab","B2.1.2"), ("hydrophobic","core barrier"),
   ("simple diffusion","B2.1.3"), ("O₂","O2 example"), ("CO₂","CO2 example"),
   ("integral","B2.1.4"), ("peripheral","B2.1.4"),
   ("osmosis","B2.1.5"), ("aquaporin","B2.1.5"), ("random movement","B2.1.5"),
   ("channel","B2.1.6"), ("facilitated diffusion","B2.1.6"),
   ("ATP","B2.1.7 pumps"), ("active transport","B2.1.7"), ("against","gradient"),
   ("selectively permeable","B2.1.8"),
   ("glycoprotein","B2.1.9"), ("glycolipid","B2.1.9"), ("extracellular","B2.1.9 carbohydrates"),
   ("unsaturated","AHL B2.1.11"), ("melting point","AHL"), ("cholesterol","AHL B2.1.12"),
   ("exocytos","AHL B2.1.13"), ("endocytos","AHL B2.1.13"),
   ("nicotinic acetylcholine","AHL B2.1.14 gated"), ("sodium and potassium channels","AHL B2.1.14"),
   ("Na⁺/K⁺","AHL B2.1.15"), ("3 Na⁺ out","AHL B2.1.15"), ("2 K⁺ in","AHL B2.1.15"), ("membrane potential","AHL B2.1.15"),
   ("cotransport","AHL B2.1.16"), ("small intestine","AHL B2.1.16"), ("indirect active transport","AHL B2.1.16"),
   ("cell-adhesion","CAM"), ("CAM","AHL B2.1.17"),
 ],
}
total_missing = 0
for topic, checks in DETAIL.items():
    f = os.path.join(BASE, topic, "index.html")
    s = open(f, encoding="utf-8", errors="replace").read()
    low = s.lower()
    miss = [ (d,note) for d,note in checks if d.lower() not in low and d not in s ]
    if miss:
        total_missing += len(miss)
        print(f"== {topic} — {len(miss)} detail gap(s) ==")
        for d,note in miss:
            print(f"   MISSING detail: {d!r}  ({note})")
print("\nTOTAL detail gaps across new topics:", total_missing)
