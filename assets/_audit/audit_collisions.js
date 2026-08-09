(() => {
  const svgs = [...document.querySelectorAll('svg')];
  const out = [];
  svgs.forEach((svg, i) => {
    const texts = [...svg.querySelectorAll('text')].map(t => {
      const r = t.getBBox();
      return { txt: (t.textContent||'').trim().slice(0,40), x: r.x, y: r.y, w: r.width, h: r.height };
    });
    const collisions = [];
    for (let a = 0; a < texts.length; a++) {
      for (let b = a+1; b < texts.length; b++) {
        const A = texts[a], B = texts[b];
        const ox = Math.min(A.x+A.w, B.x+B.w) - Math.max(A.x, B.x);
        const oy = Math.min(A.y+A.h, B.y+B.h) - Math.max(A.y, B.y);
        if (ox > 1 && oy > 1) {
          collisions.push('['+a+':'+b+'] "'+A.txt+'" x "'+B.txt+'" ('+ox.toFixed(1)+'x'+oy.toFixed(1)+'px)');
        }
      }
    }
    out.push('FIG'+i+': '+texts.length+' texts '+(collisions.length ? 'COLLISIONS: '+collisions.join(' | ') : 'clean'));
  });
  return out.join('\n');
})()
