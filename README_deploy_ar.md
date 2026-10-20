# دليل نشر موقع بيروني بريدج (GitHub + Netlify) — خطوة بخطوة

> هذا الملف لمحمد. لم يُنشأ أي مستودع ولم يُنشر أي شيء. كل الخطوات أدناه تقوم بها أنت بحساباتك.
> الموقع ثابت (HTML/CSS/JS) ولا يحتاج إلى «بناء» على Netlify. الملف `netlify.toml` يضبط كل شيء تلقائيًا (التحويل حسب اللغة، صفحات 404، رؤوس الأمان).

---

## 0) قبل أن تبدأ: قائمة ما يجب حسمه قبل ربط الدومين (مهم)
1. **الوسوم المتبقية «يُؤكَّد / TBC»** ما زالت ظاهرة في بعض الصفحات عمدًا، حتى لا يُنشر ادعاء غير مؤكَّد. القائمة الكاملة وأسبابها في رسالة التسليم. احسمها مع المستشفى ثم عدّل النص (أو احذف الجملة) قبل ربط birunibridge.com.
2. **المراجعة القانونية:** نصوص الخصوصية/KVKK، وملفات الارتباط، وإخلاء المسؤولية الطبية، ونص الموافقة في النموذج، ويجب أن يراجعها محامو المستشفى. أكّد معهم أيضًا الاسم القانوني للجهة المسؤولة عن البيانات وتسجيلها في VERBİS.
3. **نقل البيانات للخارج:** بيانات نموذج التواصل تُحفظ لدى Netlify (الولايات المتحدة). النص الحالي يطلب موافقة صريحة على ذلك؛ واسأل المحامي أيضًا عن العقد القياسي/إخطار هيئة KVKK إن لزم.
4. **شعار HealthTürkiye:** إذا كان المستشفى ملزمًا بعرضه، أرسل ملف الشعار لنضيفه في التذييل.
5. **البريد info@birunibridge.com** يجب أن يعمل ويستقبل الرسائل، لأن الموقع يوجّه المرضى لإرسال التقارير إليه. وكذلك رقم واتساب ‎+90 536 842 55 97. **لتغيير رقم واتساب** (إن أعطاك المستشفى رقمًا آخر): غيّر القيمة الوحيدة `WHATSAPP_NUMBER` في الملف `src/common.py` ثم أعد البناء بـ `python3 src/deploy.py`؛ يتغيّر الرقم والرابط في كل الصفحات واللغات السبع.
6. **مراجعة لغوية:** النصوص الروسية والإسبانية والفرنسية والأردية والفارسية مسودّات تحتاج مراجعة متحدث أصلي (ويُفضَّل مراجعة طبية وقانونية للصفحات القانونية)، والعربية الطبية تحتاج تدقيقًا. وتأكّد أن لدى الفريق منسّقين يتحدثون الأردية والفارسية قبل إطلاق هاتين النسختين (الجملة معلَّمة «يُؤكَّد» في الموقع).

---

## 1) جهّز الملفات
1. فك ضغط `birunibridge_deploy.zip` على جهازك؛ سيظهر مجلد واحد اسمه `birunibridge_site_deploy`. **ارفع محتويات هذا المجلد** (وليس المجلد نفسه) إلى المستودع. داخله مجلدات: `ar/` و`en/` و`ru/` و`es/` و`fr/` و`ur/` و`fa/` و`assets/`، و`media/` بعد فك أجزاء الفيديو، وملفات: `index.html` و`404.html` و`netlify.toml` و`sitemap.xml` و`robots.txt` و`favicon.ico`.
2. **مهم:** يجب أن يكون `netlify.toml` في **جذر** المستودع (وليس داخل مجلد فرعي).
3. **الفيديوهات (مجلد `media/`):** الفيديوهات ليست داخل `birunibridge_deploy.zip`، حتى يبقى حجمه أقل من 25 MB. هي في ملفات منفصلة اسمها `birunibridge_media_part1of5.zip` إلى `part5of5.zip`، وكل ملف أقل من 25 MB. فك ضغط **الأجزاء الخمسة كلها في المكان نفسه** الذي فككت فيه ملف الموقع، فيظهر المجلد `birunibridge_site_deploy/media/`. فيه 7 فيديوهات MP4 والمجلد `posters/`.
   - **يجب رفع `media/` إلى المستودع أيضًا**، وإلا ستظهر مشغلات الفيديو فارغة. حجمه نحو 95 MB، وكل ملف أقل من 25 MB، فيمكن رفعه حتى من واجهة GitHub في المتصفح (حدّها 25 MB للملف)، وحد GitHub 100 MB للملف.
   - اقتراح لاحق: ارفع الفيديوهات الكاملة إلى YouTube أو Vimeo. انظر `video_hosting_ar.md`.

## 2) أنشئ مستودع GitHub
1. ادخل إلى https://github.com وسجّل الدخول (أو أنشئ حسابًا).
2. اضغط **+** أعلى اليمين ← **New repository**.
3. الاسم المقترح: `birunibridge-site`. اختر **Private**. **لا** تضع علامة على "Add a README".
4. اضغط **Create repository**.

## 3) ارفع الملفات إلى GitHub (اختر طريقة واحدة)
**الطريقة أ: GitHub Desktop (الأسهل لعدد كبير من الملفات)**
1. نزّل GitHub Desktop من https://desktop.github.com وسجّل الدخول.
2. File ← Clone repository ← اختر `birunibridge-site` ← حدّد مجلدًا على جهازك.
3. انسخ **محتويات** مجلد deploy (وليس المجلد نفسه) إلى مجلد المستودع الذي أنشأه البرنامج.
4. في GitHub Desktop اكتب في خانة Summary: `first version` ← **Commit to main** ← **Push origin**.

**الطريقة ب: من المتصفح**
1. في صفحة المستودع اضغط **uploading an existing file**.
2. اسحب **محتويات** مجلد deploy. (واجهة الويب تقبل نحو 100 ملف في كل مرة، والموقع نحو 370 ملفًا، لذلك ارفع على دفعات: أولًا الملفات في الجذر مع `assets/`، ثم `ar/`، ثم `en/`، ثم `ru/` و`es/`، ثم `fr/` و`ur/` و`fa/`، وأخيرًا `media/`، فيديو أو فيديوهان في كل دفعة.) تأكد أن بنية المجلدات بقيت كما هي.
3. اضغط **Commit changes** بعد كل دفعة.

**الطريقة ج: سطر الأوامر (لمن يستخدم git)**
```
cd deploy
git init && git add . && git commit -m "first version"
git branch -M main
git remote add origin https://github.com/<اسم-حسابك>/birunibridge-site.git
git push -u origin main
```

## 4) اربط Netlify بالمستودع
1. ادخل إلى https://app.netlify.com وسجّل الدخول بحساب GitHub.
2. **Add new site** (أو Add new project) ← **Import an existing project** ← **GitHub** ← وافق على الصلاحيات ← اختر `birunibridge-site`.
3. الإعدادات: Branch = `main` · Build command = **اتركه فارغًا** · Publish directory = `.` (نقطة) · ثم **Deploy**.
4. بعد دقيقة سيظهر رابط تجريبي مثل `https://xxxx.netlify.app`. افتحه وجرّب: `/ar/` و`/en/` و`/ru/` و`/es/` و`/fr/` و`/ur/` و`/fa/`.

## 5) فعّل نموذج التواصل (Netlify Forms)
1. في لوحة الموقع: **Project configuration / Site configuration ← Forms ← Enable form detection**.
2. أعد النشر: **Deploys ← Trigger deploy ← Clear cache and deploy site** (حتى يكتشف Netlify النموذج `contact`).
3. الإشعارات: **Forms ← Form notifications ← Add notification ← Email notification** ← البريد: `info@birunibridge.com` ← Form: `contact`.
4. اختبر بنفسك: املأ النموذج في `/ar/contact/` وضع علامة الموافقة واضغط «إرسال». يجب أن تظهر صفحة «شكرًا لك»، وأن تصل الرسالة إلى Forms في Netlify وإلى البريد.
5. ملاحظة: النموذج **لا يرفع ملفات طبية**. التقارير تُرسل عبر واتساب أو info@birunibridge.com، والصفحات توضح ذلك للمريض.
6. الحماية من الرسائل المزعجة: النموذج فيه حقل خفي (honeypot)، ويمكنك أيضًا تفعيل فلتر Netlify التلقائي للسبام من إعدادات Forms.

## 6) اربط الدومين birunibridge.com
1. في Netlify: **Domain management ← Add a domain ←** اكتب `birunibridge.com` ← Verify ← **Add domain**. سيضيف Netlify تلقائيًا `www.birunibridge.com`.
2. اختر طريقة DNS:

**الخيار 1 (موصى به): DNS من Netlify**
- اختر **Set up Netlify DNS** وتابع. سيعطيك Netlify أربعة أسماء خوادم (مثل `dns1.p0X.nsone.net`…).
- **قبل التغيير:** انسخ كل سجلات البريد الحالية من مزوّد الدومين (MX وTXT/SPF وDKIM وأي CNAME للبريد) وأضفها في Netlify DNS، **وإلا سيتوقف البريد** info@birunibridge.com.
- عند مسجّل الدومين (حيث اشتريت الدومين): غيّر **Nameservers** إلى أسماء Netlify الأربعة واحفظ.

**الخيار 2: تبقي DNS عند المسجّل الحالي**
- أضف/عدّل السجلات التالية فقط (ولا تلمس سجلات MX الخاصة بالبريد):

| النوع | الاسم/Host | القيمة |
|---|---|---|
| ALIAS أو ANAME أو flattened CNAME (إن كان مدعومًا) | `@` | `apex-loadbalancer.netlify.com` |
| أو بدلًا منه: A | `@` | `75.2.60.5` |
| CNAME | `www` | `اسم-موقعك.netlify.app` |

- احذف أي سجل A آخر للجذر `@`، وأي سجلات **AAAA** قديمة، لأنها تمنع إصدار شهادة HTTPS.

3. انتظر الانتشار (من دقائق حتى 24–48 ساعة). تحقق عبر https://dnschecker.org.
4. **HTTPS:** في Domain management ← HTTPS، يصدر Netlify شهادة Let’s Encrypt تلقائيًا بعد انتشار DNS. إن لم تصدر خلال ساعات اضغط **Verify DNS configuration** ثم **Provision certificate**.
5. اجعل `birunibridge.com` هو **Primary domain** (والملف `netlify.toml` يحوّل www إليه).

## 7) تحقق نهائي بعد الربط
- `https://birunibridge.com/` يحوّلك حسب لغة متصفحك: العربية ← `/ar/`، والروسية ← `/ru/`، والإسبانية ← `/es/`، والفرنسية ← `/fr/`، والأردية ← `/ur/`، والفارسية ← `/fa/`، وغيرها ← `/en/`.
- جرّب رابطًا غير موجود مثل `/ar/xyz` لترى صفحة 404 العربية.
- شريط ملفات الارتباط يظهر في أول زيارة، ولا تُحمَّل الخريطة إلا بعد الموافقة على «الخرائط والمحتوى الخارجي».
- `https://birunibridge.com/sitemap.xml` و`/robots.txt` يفتحان.
- أرسل نموذجًا تجريبيًا من كل لغة.
- (اختياري) أضف الموقع في Google Search Console وأرسل `sitemap.xml`.

## 8) التعديلات لاحقًا
- **تعديل بسيط:** افتح الملف في GitHub (مثل `ar/index.html`) ← أيقونة القلم ← عدّل ← Commit. سينشر Netlify التحديث تلقائيًا خلال دقيقة.
- **تعديل شامل:** النصوص الأصلية في مولّدات Python داخل `/workspace/birunibridge_site/src/`. نعدّلها ثم نشغّل `python3 src/deploy.py` لإعادة بناء المجلد `deploy/`، ثم ترفع الملفات الجديدة.
- **لا تضف أي أداة إحصاء** (Google Analytics أو Meta Pixel…) قبل تحديث سياسة ملفات الارتباط، ويجب أن تُحمَّل فقط بعد الموافقة. يوجد مكان مخصص لذلك في `assets/site.js` (الدالة `bbLoadAnalytics`).

## 9) ما الذي يفعله netlify.toml
- تحويل `www` إلى `birunibridge.com`.
- تحويل الجذر `/` حسب لغة المتصفح (ar/ru/es/fr/ur/fa، والافتراضي en).
- صفحة 404 لكل لغة.
- رؤوس أمان: HSTS، وX-Frame-Options، وX-Content-Type-Options، وReferrer-Policy، وPermissions-Policy، وسياسة CSP تسمح فقط بموارد الموقع نفسه وبخرائط Google بعد الموافقة.
- `noindex` لصفحات «شكرًا لك».

## جدول العملاء المحتملين (Google Sheets)
النموذج يرسل إلى Netlify Forms كما هو، ويرسل نسخة من الحقول نفسها إلى جدول Google عبر Apps Script. الإعداد في `google_sheet_setup_ar.md`، والسكربت في `google_sheet/Code.gs`. الرابط والرمز في `src/common.py` (`SHEET_WEBHOOK_URL`, `SHEET_TOKEN`). إذا كان الرابط فارغًا فلا يُرسل شيء إلى الجدول.
