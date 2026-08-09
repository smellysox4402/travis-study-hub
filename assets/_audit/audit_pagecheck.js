(() => {
  const r = {};
  r.svgs = document.querySelectorAll('svg').length;
  r.ariaLabels = document.querySelectorAll('svg[aria-label]').length;
  r.homeLinks = [...document.querySelectorAll('a')].filter(a => a.textContent.trim() === 'HOME' || (a.getAttribute('href')||'').includes('index.html')).length;
  r.favicons = document.querySelectorAll('link[rel="icon"]').length;
  r.quizRadios = document.querySelectorAll('input[type="radio"]').length;
  r.quizQuestions = document.querySelectorAll('.q').length;
  r.checklistItems = document.querySelectorAll('#cl li').length;
  r.acts = document.querySelectorAll('section.act').length;
  r.mindNodes = document.querySelectorAll('.mind .node').length;
  r.cheatLines = document.querySelectorAll('.marquee .line').length;
  r.burps = (document.documentElement.outerHTML.match(/burp/gi)||[]).length;
  return JSON.stringify(r);
})()
