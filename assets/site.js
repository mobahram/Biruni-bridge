window.BB_SHEET={"url": "", "token": "VZ-efZ4eaLgslNm_f6zpL9wK_GE3069n"};
window.BB_GFORM={"action": "https://docs.google.com/forms/d/e/1FAIpQLScw8zb6VkHO7Vg7qWUZeUc6Gv4maiXmIg7jQ2mDaPsTnets6g/formResponse", "entries": {"lang": "entry.382130787", "name": "entry.1048378349", "country": "entry.872875437", "phone": "entry.79439632", "email": "entry.1325751394", "specialty": "entry.1000958012", "kvkk_consent": "entry.45530695", "message": "entry.2119470668"}};
/* Biruni Bridge site script: consent (no tracking before consent), mobile menu, FAQ search, consent-gated map */
(function(){
  var KEY='bb_consent', DAYS=365;
  function get(){try{var c=JSON.parse(localStorage.getItem(KEY)||'null');if(c&&Date.now()-c.ts<DAYS*864e5)return c}catch(e){}return null}
  function set(c){c.ts=Date.now();try{localStorage.setItem(KEY,JSON.stringify(c))}catch(e){}apply(c)}
  function apply(c){
    if(c&&c.media){document.querySelectorAll('[data-map]').forEach(function(m){if(m.classList.contains('loaded'))return;var f=document.createElement('iframe');f.src='https://www.google.com/maps?q=Istanbul&output=embed';f.loading='lazy';f.title='Map';f.referrerPolicy='no-referrer-when-downgrade';m.innerHTML='';m.appendChild(f);m.classList.add('loaded')})}
    if(c&&c.analytics&&typeof window.bbLoadAnalytics==='function'){window.bbLoadAnalytics()} /* no analytics configured yet */
  }
  var ck=document.getElementById('ck');
  function open(settings){if(!ck)return;ck.hidden=false;var o=ck.querySelector('.ck-opts'),s=ck.querySelector('[data-ck=save]'),g=ck.querySelector('[data-ck=settings]');var c=get()||{};
    document.getElementById('ck-media').checked=!!c.media;document.getElementById('ck-an').checked=!!c.analytics;o.hidden=!settings;s.hidden=!settings;g.hidden=!!settings}
  if(ck){ck.addEventListener('click',function(e){var b=e.target.closest('[data-ck]');if(!b)return;var a=b.getAttribute('data-ck');
      if(a==='accept'){set({necessary:true,media:true,analytics:true});ck.hidden=true}
      else if(a==='reject'){set({necessary:true,media:false,analytics:false});ck.hidden=true}
      else if(a==='settings'){open(true)}
      else if(a==='save'){set({necessary:true,media:document.getElementById('ck-media').checked,analytics:document.getElementById('ck-an').checked});ck.hidden=true}});
    var c=get(); if(c){apply(c)}else{open(false)}}
  document.querySelectorAll('[data-ck-open]').forEach(function(b){b.addEventListener('click',function(){open(true)})});
  /* GA4 events. The gtag snippet lives in each page head. Never send name, phone, email, message, or other personal or medical fields. */
  function pageLanguage(){return document.documentElement.getAttribute('lang')||'';}
  function track(name,params){try{if(typeof gtag==='function')gtag('event',name,params);}catch(err){}}
  function linkLocation(el){
    if(el.closest('.fab'))return 'floating';
    if(el.closest('.topbar, header'))return 'header';
    if(el.closest('#contact, #form, form[name=contact], .fcard, .wa-card, .ccards, .contacts, .repbox'))return 'contact_section';
    if(el.closest('footer'))return 'footer';
    if(el.closest('.hero'))return 'hero';
    return 'content';
  }
  function trackLead(f){
    var pref=f.elements.preferred_language;
    track('generate_lead',{page_language:pageLanguage(),preferred_language:pref?String(pref.value||''):'',form_location:location.pathname});
  }
  /* contact form: Netlify Forms submission stays the normal POST; a copy of the same fields goes to the Google Sheet (Apps Script) if configured */
  var SH=window.BB_SHEET||{},GF=window.BB_GFORM||{};
  document.querySelectorAll('form[name=contact]').forEach(function(f){
    f.addEventListener('submit',function(e){
      var bot=f.querySelector('[name=bot-field]');
      if(!f.getAttribute('data-sent')&&!(bot&&bot.value))trackLead(f);
      if((!SH.url&&!GF.action)||f.getAttribute('data-sent'))return;  /* nothing configured -> plain Netlify submit */
      var hp=f.querySelector('[name=bot-field]');if(hp&&hp.value)return;
      e.preventDefault();f.setAttribute('data-sent','1');
      var d={token:SH.token,page:location.pathname};
      ['lang','source_page','name','country','phone','email','specialty','message','preferred_language'].forEach(function(n){var el=f.elements[n];if(el)d[n]=String(el.value||'').trim().slice(0,n==='message'?1500:200)});
      d.kvkk_consent=f.elements.kvkk_consent&&f.elements.kvkk_consent.checked?'yes':'';
      d.marketing_consent=f.elements.marketing_consent&&f.elements.marketing_consent.checked?'yes':'no';
      var note='\n\n[Page: '+(d.source_page||d.page||'')+' | Marketing consent: '+d.marketing_consent+' | Preferred language: '+(d.preferred_language||'-')+']';
      if(f.elements.message){f.elements.message.value=(d.message||'-')+note}
      var done=false,go=function(){if(done)return;done=true;HTMLFormElement.prototype.submit.call(f)};
      var jobs=[];
      try{if(SH.url)jobs.push(fetch(SH.url,{method:'POST',mode:'no-cors',keepalive:true,headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(d)}))}catch(x){}
      try{if(GF.action&&GF.entries){var q=new URLSearchParams();var g={};Object.keys(d).forEach(function(k){g[k]=d[k]});g.message=(d.message||'-')+note;Object.keys(GF.entries).forEach(function(k){if(k!=='token')q.append(GF.entries[k],(g[k]===undefined||g[k]==='')?'-':g[k])});
        jobs.push(fetch(GF.action,{method:'POST',mode:'no-cors',keepalive:true,headers:{'Content-Type':'application/x-www-form-urlencoded'},body:q.toString()}))}}catch(x){}
      if(!jobs.length){go()}else{var left=jobs.length;jobs.forEach(function(j){j.then(function(){if(--left===0)go()},function(){if(--left===0)go()})})}
      setTimeout(go,2500);                                          /* never block the Netlify submission */
    });
  });
  /* videos: preload=none; poster image only when the player comes near the viewport */
  var vs=document.querySelectorAll('video[data-poster]');
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.poster=e.target.getAttribute('data-poster');io.unobserve(e.target)}})},{rootMargin:'300px'});vs.forEach(function(v){io.observe(v)})}
  else{vs.forEach(function(v){v.poster=v.getAttribute('data-poster')})}
  /* only one video plays at a time */
  document.addEventListener('play',function(e){document.querySelectorAll('video').forEach(function(v){if(v!==e.target)v.pause()})},true);
  /* mobile menu */
  var bg=document.querySelector('.burger'),hd=document.querySelector('header.main');
  if(bg&&hd){bg.addEventListener('click',function(){var o=hd.classList.toggle('open');bg.setAttribute('aria-expanded',o?'true':'false')})}
  /* FAQ search */
  var sb=document.querySelector('.search input');
  if(sb){var run=function(){var v=sb.value.trim().toLowerCase();document.querySelectorAll('.fqcat').forEach(function(cat){var any=false;cat.querySelectorAll('details').forEach(function(d){var ok=!v||d.textContent.toLowerCase().indexOf(v)>-1;d.classList.toggle('hide',!ok);if(ok)any=true;if(v&&ok)d.open=true});cat.classList.toggle('hide',!any)})};
    sb.addEventListener('input',run);var sbtn=document.querySelector(".search .btn");if(sbtn)sbtn.addEventListener('click',function(e){e.preventDefault();run()})}
  document.addEventListener('click',function(e){
    var a=e.target&&e.target.closest?e.target.closest('a'):null;
    if(!a)return;
    var href=a.getAttribute('href')||'';
    var params={page_language:pageLanguage(),link_location:linkLocation(a)};
    if(/wa\.me|api\.whatsapp\.com/i.test(href)||a.classList.contains('fab'))track('whatsapp_click',params);
    else if(/^mailto:/i.test(href))track('email_click',params);
    else if(/^tel:/i.test(href))track('phone_click',params);
  },true);
})();
