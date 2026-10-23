"""Spanish, French, Urdu and Persian FAQ, plus journey, check-up, cellular and oncology."""

from __future__ import annotations


def _cart(lang: str, label: str) -> str:
    return f'<a href="/{lang}/car-t-cell-therapy-turkey/">{label}</a>'


FAQ_MORE = {
    "es": {
        "title": "Preguntas frecuentes | Biruni Bridge",
        "description": "Respuestas sobre informes, planes, coste, visado, estancia, seguimiento y terapia celular CAR-T.",
        "h1": "Preguntas y respuestas para pacientes internacionales",
        "sub": "Respuestas claras sobre informes, planes, coste, viaje, tratamiento, seguimiento y privacidad.",
        "crumb": "Preguntas frecuentes",
        "miss_h": "¿No encontró su respuesta?",
        "miss_p": "Pregunte al coordinador por WhatsApp o envíe su informe.",
        "ask_h": "Consúltenos su caso",
        "ask_p": "Un coordinador responde en su idioma.",
        "cats": [
            ("Antes de viajar", [
                ("¿Cómo empiezo?", "Envíe sus informes por WhatsApp o a info@birunibridge.com, o deje sus datos en el formulario. Un coordinador que habla su idioma le contactará y pedirá lo que falte."),
                ("¿Qué documentos debo enviar?", "El informe médico más reciente, informes de imagen (se prefieren imágenes DICOM), biopsia si la hay, análisis de sangre recientes y una lista fechada de tratamientos previos."),
                ("¿La revisión inicial es gratuita?", "Sí. La revisión a distancia de su expediente es gratuita y no le compromete a nada."),
            ]),
            ("Informes y plan", [
                ("¿Cuándo recibiré el plan?", "Habitualmente en 24–48 horas desde un expediente completo. Los casos complejos pueden tardar más."),
                ("¿Quién revisa mi expediente?", "Médicos de la especialidad correspondiente y, en casos complejos, varias especialidades."),
                ("¿El plan es definitivo?", "Es un plan propuesto. Puede cambiar tras la valoración a la llegada; cualquier cambio se explica antes de empezar."),
            ]),
            ("Coste y seguro", [
                ("¿Cuánto cuesta el tratamiento?", "El coste se valora caso por caso después de revisar su informe médico."),
                ("¿Trabajan con aseguradoras internacionales?", "En muchos casos, mediante autorización previa o facturación directa."),
            ]),
            ("Viaje y estancia", [
                ("¿Ayudan con el visado y el alojamiento?", "Sí. Carta de invitación médica, recogida en el aeropuerto, traslado y alojamiento para usted y su acompañante."),
                ("¿Hay intérpretes?", "Sí, las 24 horas."),
            ]),
            ("Durante el tratamiento", [
                ("¿Quién me acompaña en el hospital?", "Su coordinador y un intérprete cuando hace falta; su acompañante puede quedarse según la norma del hospital."),
                ("¿Y si necesito quedarme más tiempo?", "Se lo decimos enseguida y ayudamos a prolongar la estancia y el visado."),
            ]),
            ("Después de volver", [
                ("¿Cómo es el seguimiento?", "Un informe de alta detallado, seguimiento a distancia y contacto con su médico local."),
            ]),
            ("Oncología y CAR-T", [
                ("¿Hay terapia de células CAR-T en el Hospital Universitario Biruni?", "Sí. La terapia CAR-T está disponible para pacientes candidatos. El equipo de hematología y trasplante decide tras revisar el expediente; no todo paciente es candidato y no se puede garantizar un resultado. " + _cart("es", "Leer: terapia CAR-T en Turquía, sus preguntas")),
                ("¿Qué es la terapia CAR-T?", "Los linfocitos T de su sangre se modifican en un laboratorio para reconocer una diana en las células tumorales (como CD19) y se devuelven en una infusión. Puede ayudar en algunos cánceres de la sangre avanzados, pero no funciona en todo el mundo. (Fuente: NCI)"),
                ("¿CAR-T significa una curación completa?", "No se puede prometer una curación. Algunos pacientes logran una remisión larga; otros no responden o recaen."),
                ("¿Quién puede ser candidato?", "Habitualmente quien recayó o no respondió al tratamiento estándar. El equipo valora el tipo de enfermedad y la diana, la salud general y la función del corazón, el riñón, el hígado y el pulmón. La decisión final es del equipo de hematología y trasplante de Biruni."),
                ("¿Qué documentos hacen falta para una revisión a distancia?", "Biopsia con inmunohistoquímica (por ejemplo CD19), informes de PET-CT, tratamientos previos con fechas, analítica reciente completa y un informe reciente. El coordinador indica si el equipo necesita algo más."),
                ("¿Cuáles son los pasos?", "Valoración, recogida de células, fabricación, a veces tratamiento puente, quimioterapia de acondicionamiento, infusión (habitualmente en menos de 30 minutos), vigilancia estrecha y seguimiento a largo plazo."),
                ("¿Cuánto tarda la fabricación?", "Habitualmente unas 3–5 semanas desde la recogida hasta la infusión (NCI). El equipo le da el plazo previsto para su caso."),
                ("¿Cuáles son los efectos principales?", "Síndrome de liberación de citocinas (fiebre, tensión baja, dificultad para respirar), toxicidad neurológica (confusión, dificultad para hablar), cifras bajas e infección; a veces el cuadro es grave."),
                ("¿Cuánto tiempo debo permanecer cerca del hospital tras la infusión?", "En algunos países la norma exige al menos dos semanas cerca de un centro especializado; muchos centros piden a los pacientes internacionales quedarse más. En Biruni el equipo fija el periodo de su caso antes del viaje."),
                ("¿Necesito un acompañante?", "Habitualmente sí: un adulto disponible a todas horas las primeras semanas. El coordinador explica cómo se organiza."),
                ("¿Cuánto cuesta?", "El coste se valora caso por caso tras revisar el informe. Pida siempre un presupuesto escrito que diga qué incluye, también las complicaciones y los cuidados intensivos."),
                ("¿Cómo es el seguimiento al volver?", "Análisis regulares, inmunoglobulinas, imagen y contacto entre el centro y su médico local; se recomienda seguimiento a largo plazo. El equipo de Biruni acuerda el plan con usted y con su médico."),
                ("¿Tratamiento aprobado o ensayo clínico?", "Un producto aprobado ha sido revisado por un regulador para un uso concreto. Un ensayo prueba un tratamiento o un uso nuevo, con un resultado menos seguro. Pida siempre el número de registro del ensayo."),
            ]),
            ("Privacidad y datos", [
                ("¿Dónde se guardan mis informes?", "Los informes que envía por WhatsApp o por correo los trata el equipo de pacientes internacionales y solo se comparten con el equipo médico que revisa su caso."),
                ("¿Puedo pedir que borren mis datos?", "Sí, conforme a sus derechos en la ley de datos personales KVKK (artículo 11)."),
            ]),
        ],
    },
    "fr": {
        "title": "Questions fréquentes | Biruni Bridge",
        "description": "Réponses sur les documents, le plan, le coût, le visa, le séjour, le suivi et la thérapie cellulaire CAR-T.",
        "h1": "Questions et réponses pour les patients internationaux",
        "sub": "Des réponses claires sur les documents, le plan, le coût, le voyage, le traitement, le suivi et la confidentialité.",
        "crumb": "Questions fréquentes",
        "miss_h": "Vous n’avez pas trouvé votre réponse ?",
        "miss_p": "Demandez au coordinateur sur WhatsApp ou envoyez votre dossier.",
        "ask_h": "Parlez-nous de votre situation",
        "ask_p": "Un coordinateur répond dans votre langue.",
        "cats": [
            ("Avant le voyage", [
                ("Comment commencer ?", "Envoyez vos documents sur WhatsApp ou à info@birunibridge.com, ou laissez vos coordonnées dans le formulaire. Un coordinateur qui parle votre langue vous contacte et demande ce qui manque."),
                ("Quels documents envoyer ?", "Le dernier compte rendu, les comptes rendus d’imagerie (images DICOM de préférence), la biopsie s’il y en a une, des analyses de sang récentes et une liste datée des traitements antérieurs."),
                ("Le premier examen du dossier est-il gratuit ?", "Oui. L’examen à distance du dossier est gratuit et ne vous engage à rien."),
            ]),
            ("Documents et plan", [
                ("Quand aurai-je le plan ?", "En général sous 24–48 heures une fois le dossier complet. Les situations complexes peuvent prendre plus de temps."),
                ("Qui lit mon dossier ?", "Des médecins de la spécialité concernée et, si le cas est complexe, plusieurs spécialités."),
                ("Le plan est-il définitif ?", "C’est un plan proposé. Il peut changer après l’évaluation à l’arrivée ; tout changement est expliqué avant de commencer."),
            ]),
            ("Coût et assurance", [
                ("Combien coûte le traitement ?", "Le coût est établi au cas par cas après l’examen de votre compte rendu médical."),
                ("Travaillez-vous avec des assureurs internationaux ?", "Dans de nombreux cas, par entente préalable ou facturation directe."),
            ]),
            ("Voyage et séjour", [
                ("Aidez-vous pour le visa et le logement ?", "Oui. Lettre d’invitation médicale, accueil à l’aéroport, transfert et logement pour vous et votre accompagnant."),
                ("Y a-t-il des interprètes ?", "Oui, 24 heures sur 24."),
            ]),
            ("Pendant le traitement", [
                ("Qui est avec moi à l’hôpital ?", "Votre coordinateur et un interprète lorsque c’est nécessaire ; votre accompagnant peut rester selon le règlement de l’hôpital."),
                ("Et si je dois rester plus longtemps ?", "Nous vous le disons tout de suite et nous aidons à prolonger le séjour et le visa."),
            ]),
            ("Après le retour", [
                ("Comment se passe le suivi ?", "Un compte rendu de sortie détaillé, un suivi à distance et le contact avec votre médecin sur place."),
            ]),
            ("Oncologie et CAR-T", [
                ("La thérapie cellulaire CAR-T est-elle disponible à l’hôpital universitaire Biruni ?", "Oui. Le CAR-T est disponible pour les patients éligibles. L’équipe d’hématologie et de greffe décide après lecture du dossier ; tout le monde n’est pas candidat et aucun résultat ne peut être garanti. " + _cart("fr", "Lire : le CAR-T en Turquie, vos questions")),
                ("Qu’est-ce que le CAR-T ?", "Des lymphocytes T de votre sang sont modifiés en laboratoire pour reconnaître une cible sur les cellules cancéreuses (comme CD19), puis rendus en une seule perfusion. Cela peut aider dans certains cancers du sang avancés, mais pas chez tout le monde. (Source : NCI)"),
                ("Le CAR-T signifie-t-il une guérison complète ?", "Une guérison ne peut pas être promise. Certains patients obtiennent une longue rémission ; d’autres ne répondent pas ou rechutent."),
                ("Qui peut être candidat ?", "En général une personne dont la maladie est revenue ou n’a pas répondu au traitement habituel. L’équipe évalue le type de maladie et la cible, l’état général, le cœur, les reins, le foie et les poumons. La décision finale revient à l’équipe d’hématologie et de greffe de Biruni."),
                ("Quels documents pour un avis à distance ?", "Biopsie avec immunomarquage (par exemple CD19), comptes rendus de TEP-TDM, traitements antérieurs avec les dates, bilan sanguin récent et un compte rendu récent. Le coordinateur vous dit si l’équipe a besoin d’autre chose."),
                ("Quelles sont les étapes ?", "Évaluation, puis recueil des cellules, fabrication, parfois traitement relais, chimiothérapie de conditionnement, perfusion (en général moins de 30 minutes), surveillance étroite et suivi au long cours."),
                ("Combien de temps dure la fabrication ?", "En général environ 3–5 semaines du recueil à la perfusion (NCI). L’équipe vous donne le délai prévu pour votre situation."),
                ("Quels sont les effets principaux ?", "Syndrome de relargage des cytokines (fièvre, tension basse, gêne respiratoire), toxicité neurologique (confusion, difficulté à parler), baisse des cellules sanguines et risque d’infection ; l’état peut parfois être grave."),
                ("Combien de temps rester près de l’hôpital après la perfusion ?", "Dans certains pays la règle demande au moins deux semaines près d’un centre spécialisé ; beaucoup de centres demandent aux patients internationaux de rester plus longtemps. À Biruni, l’équipe fixe la durée de votre cas avant le voyage."),
                ("Faut-il un accompagnant ?", "En général oui : un adulte joignable à toute heure les premières semaines. Le coordinateur explique l’organisation."),
                ("Combien cela coûte-t-il ?", "Le coût est établi au cas par cas après lecture du compte rendu. Demandez un devis écrit qui précise ce qui est compris, y compris les complications et la réanimation."),
                ("Comment se passe le suivi au retour ?", "Analyses régulières, immunoglobulines, imagerie et contact entre le centre et votre médecin ; un suivi au long cours est recommandé. L’équipe de Biruni convient du plan avec vous et avec votre médecin."),
                ("Produit autorisé ou essai clinique ?", "Un produit autorisé a été examiné par une autorité pour un usage précis. Un essai teste un traitement ou un usage nouveau, avec un résultat moins certain. Demandez toujours le numéro d’enregistrement de l’essai."),
            ]),
            ("Confidentialité", [
                ("Où sont conservés mes documents ?", "Les documents envoyés par WhatsApp ou par e-mail sont traités par l’équipe des patients internationaux et partagés seulement avec l’équipe médicale qui examine votre dossier."),
                ("Puis-je demander l’effacement de mes données ?", "Oui, au titre de vos droits dans la loi turque sur les données personnelles KVKK (article 11)."),
            ]),
        ],
    },
    "ur": {
        "title": "عام سوالات | Biruni Bridge",
        "description": "رپورٹس، منصوبہ، لاگت، ویزا، قیام، فالو اپ اور CAR-T سیل تھراپی کے بارے میں جوابات۔",
        "h1": "بین الاقوامی مریضوں کے لیے سوالات اور جوابات",
        "sub": "رپورٹس، منصوبہ، لاگت، سفر، علاج، فالو اپ اور رازداری کے واضح جواب۔",
        "crumb": "عام سوالات",
        "miss_h": "جواب نہیں ملا؟",
        "miss_p": "کوآرڈینیٹر سے WhatsApp پر پوچھیں یا اپنی رپورٹ بھیجیں۔",
        "ask_h": "اپنے کیس کے بارے میں پوچھیں",
        "ask_p": "کوآرڈینیٹر آپ کی زبان میں جواب دیتا ہے۔",
        "cats": [
            ("سفر سے پہلے", [
                ("آغاز کیسے کروں؟", "رپورٹس WhatsApp پر یا info@birunibridge.com پر بھیجیں، یا فارم میں اپنی تفصیل لکھیں۔ آپ کی زبان بولنے والا کوآرڈینیٹر رابطہ کرے گا اور جو چیز کم ہو وہ مانگے گا۔"),
                ("کون سی دستاویزات بھیجوں؟", "تازہ ترین میڈیکل رپورٹ، امیجنگ رپورٹس (DICOM تصاویر بہتر ہیں)، بایپسی اگر ہوئی ہو، حالیہ خون کے ٹیسٹ، اور پچھلے علاج کی تاریخ کے ساتھ فہرست۔"),
                ("ابتدائی جائزہ مفت ہے؟", "ہاں۔ فائل کا یہ فاصلاتی جائزہ مفت ہے اور آپ کو کسی چیز کا پابند نہیں کرتا۔"),
            ]),
            ("رپورٹس اور منصوبہ", [
                ("منصوبہ کب ملے گا؟", "مکمل فائل کے بعد عموماً 24–48 گھنٹوں میں۔ پیچیدہ کیس میں زیادہ وقت لگ سکتا ہے۔"),
                ("فائل کون دیکھتا ہے؟", "متعلقہ شعبے کے معالج، اور پیچیدہ کیس میں کئی شعبے۔"),
                ("کیا منصوبہ حتمی ہے؟", "یہ تجویز کردہ منصوبہ ہے۔ آمد کے بعد جائزے سے بدل سکتا ہے؛ ہر تبدیلی علاج شروع ہونے سے پہلے سمجھا دی جاتی ہے۔"),
            ]),
            ("لاگت اور انشورنس", [
                ("علاج کی لاگت کتنی ہے؟", "لاگت میڈیکل رپورٹ کے جائزے کے بعد ہر کیس کے حساب سے طے ہوتی ہے۔"),
                ("کیا آپ بین الاقوامی انشورنس کے ساتھ کام کرتے ہیں؟", "بہت سے کیسوں میں پیشگی اجازت یا براہ راست بل کے ذریعے۔"),
            ]),
            ("سفر اور قیام", [
                ("ویزا اور رہائش میں مدد ملتی ہے؟", "ہاں۔ طبی دعوت نامہ، ہوائی اڈے پر استقبال، ٹرانسفر، اور آپ کے اور ساتھی کے لیے رہائش۔"),
                ("کیا مترجم دستیاب ہیں؟", "ہاں، چوبیس گھنٹے۔"),
            ]),
            ("علاج کے دوران", [
                ("ہسپتال میں میرے ساتھ کون ہوگا؟", "آپ کا کوآرڈینیٹر اور ضرورت پر مترجم؛ ساتھی ہسپتال کے قاعدے کے مطابق رہ سکتا ہے۔"),
                ("اگر زیادہ رہنا پڑے؟", "ہم فوراً بتاتے ہیں اور قیام اور ویزا بڑھانے میں مدد کرتے ہیں۔"),
            ]),
            ("واپسی کے بعد", [
                ("فالو اپ کیسے ہوتا ہے؟", "تفصیلی ڈسچارج خلاصہ، فاصلاتی فالو اپ، اور آپ کے مقامی معالج سے رابطہ۔"),
            ]),
            ("آنکولوجی اور CAR-T", [
                ("کیا Biruni یونیورسٹی ہسپتال میں CAR-T سیل تھراپی موجود ہے؟", "ہاں۔ موزوں مریضوں کے لیے CAR-T دستیاب ہے۔ ہیماٹولوجی اور ٹرانسپلانٹ ٹیم فائل دیکھ کر فیصلہ کرتی ہے؛ ہر مریض امیدوار نہیں ہوتا اور نتیجہ کی ضمانت نہیں دی جا سکتی۔ " + _cart("ur", "پڑھیں: ترکی میں CAR-T، آپ کے سوالات")),
                ("CAR-T کیا ہے؟", "آپ کے خون کے ٹی سیلز تجربہ گاہ میں اس طرح بدلے جاتے ہیں کہ وہ کینسر کے خلیوں پر ایک نشان (جیسے CD19) پہچانیں، پھر ایک انفیوژن میں واپس دیے جاتے ہیں۔ یہ خون کے کچھ پیشرفته کینسر میں مدد کر سکتا ہے، مگر ہر شخص میں نہیں۔ (ماخذ: NCI)"),
                ("کیا CAR-T کا مطلب مکمل شفا ہے؟", "شفا کا وعدہ نہیں کیا جا سکتا۔ کچھ مریضوں میں لمبی معافی ہوتی ہے؛ کچھ جواب نہیں دیتے یا بیماری لوٹ آتی ہے۔"),
                ("کون امیدوار ہو سکتا ہے؟", "عموماً وہ مریض جن کی بیماری لوٹ آئی ہو یا معیاری علاج سے جواب نہ ملا ہو۔ ٹیم بیماری کی قسم اور نشان، عمومی صحت، دل، گردہ، جگر اور پھیپھڑے دیکھتی ہے۔ حتمی فیصلہ Biruni کی ہیماٹولوجی اور ٹرانسپلانٹ ٹیم کرتی ہے۔"),
                ("فاصلاتی جائزے کے لیے کون سی دستاویزات چاہیے؟", "امیونوسٹیننگ کے ساتھ بایپسی (مثلاً CD19)، PET-CT رپورٹس، تاریخوں کے ساتھ پچھلا علاج، حالیہ مکمل خون کے ٹیسٹ، اور تازہ رپورٹ۔ اگر ٹیم کو اور کچھ چاہیے تو کوآرڈینیٹر بتاتا ہے۔"),
                ("مراحل کیا ہیں؟", "جائزہ، پھر خلیات کا حصول، تیاری، کبھی عبوری علاج، کنڈیشننگ کیموتھراپی، انفیوژن (عموماً 30 منٹ سے کم)، پھر قریبی نگرانی اور طویل فالو اپ۔"),
                ("تیاری میں کتنا وقت لگتا ہے؟", "حصول سے انفیوژن تک عموماً تقریباً 3–5 ہفتے (NCI)۔ ٹیم آپ کے کیس کا متوقع وقت بتاتی ہے۔"),
                ("اہم ضمنی اثرات کیا ہیں؟", "سائٹوکائن ریلیز سنڈروم (بخار، کم فشار، سانس میں دشواری)، اعصابی زہریلا پن (الجھن، بولنے میں دشواری)، خون کے خلیات میں کمی اور انفیکشن کا خطرہ؛ کبھی حالت سنگین ہو سکتی ہے۔"),
                ("انفیوژن کے بعد ہسپتال کے قریب کتنی دیر رہنا ہوتا ہے؟", "کچھ ممالک میں معیار کم از کم دو ہفتے کسی ماہر مرکز کے قریب رہنے کا ہے؛ بہت سے مراکز بین الاقوامی مریضوں سے زیادہ قیام مانگتے ہیں۔ Biruni میں ٹیم سفر سے پہلے آپ کے کیس کی مدت طے کرتی ہے۔"),
                ("کیا ساتھی ضروری ہے؟", "عموماً ہاں: پہلے ہفتوں میں چوبیس گھنٹے دستیاب ایک بالغ۔ کوآرڈینیٹر انتظام سمجھاتا ہے۔"),
                ("لاگت کتنی ہے؟", "رپورٹ کے جائزے کے بعد لاگت ہر کیس پر الگ ہوتی ہے۔ تحریری تخمینہ مانگیں جس میں یہ لکھا ہو کہ کیا شامل ہے، بشمول پیچیدگیاں اور انتہائی نگہداشت۔"),
                ("واپسی کے بعد فالو اپ کیسے ہوتا ہے؟", "باقاعدہ خون کے ٹیسٹ، امیونوگلوبلین، امیجنگ، اور مرکز کا آپ کے مقامی معالج سے رابطہ؛ طویل فالو اپ تجویز کیا جاتا ہے۔ Biruni کی ٹیم منصوبہ آپ سے اور آپ کے معالج سے طے کرتی ہے۔"),
                ("منظور شدہ علاج یا کلینیکل ٹرائل؟", "منظور شدہ پروڈکٹ کو ایک ریگولیٹر نے مخصوص استعمال کے لیے دیکھا ہوتا ہے۔ ٹرائل نیا علاج یا نیا استعمال آزماتا ہے، جس کا نتیجہ کم یقینی ہوتا ہے۔ ہمیشہ ٹرائل کا رجسٹریشن نمبر مانگیں۔"),
            ]),
            ("رازداری", [
                ("میری رپورٹس کہاں رکھی جاتی ہیں؟", "WhatsApp یا ای میل سے بھیجی گئی رپورٹس بین الاقوامی مریض ٹیم سنبھالتی ہے اور صرف اسی طبی ٹیم کو دیتی ہے جو آپ کا کیس دیکھ رہی ہو۔"),
                ("کیا میں اپنے ڈیٹا کے حذف کی درخواست کر سکتا ہوں؟", "ہاں، KVKK کے ذاتی ڈیٹا کے قانون کے حقوق کے تحت (دفعہ 11)۔"),
            ]),
        ],
    },
    "fa": {
        "title": "پرسش‌های متداول | Biruni Bridge",
        "description": "پاسخ دربارهٔ گزارش‌ها، برنامه، هزینه، ویزا، اقامت، پیگیری و درمان سلولی CAR-T.",
        "h1": "پرسش و پاسخ برای بیماران بین‌المللی",
        "sub": "پاسخ‌های روشن دربارهٔ گزارش‌ها، برنامه، هزینه، سفر، درمان، پیگیری و حریم خصوصی.",
        "crumb": "پرسش‌های متداول",
        "miss_h": "پاسخ خود را پیدا نکردید؟",
        "miss_p": "از هماهنگ‌کننده در واتساپ بپرسید یا گزارش را بفرستید.",
        "ask_h": "دربارهٔ پرونده‌تان بپرسید",
        "ask_p": "هماهنگ‌کننده‌ای به زبان شما پاسخ می‌دهد.",
        "cats": [
            ("پیش از سفر", [
                ("چگونه شروع کنم؟", "گزارش‌ها را در واتساپ یا به info@birunibridge.com بفرستید، یا مشخصات را در فرم بگذارید. هماهنگ‌کننده‌ای که زبان شما را می‌داند تماس می‌گیرد و هر چه کم باشد می‌پرسد."),
                ("چه مدارکی بفرستم؟", "تازه‌ترین گزارش پزشکی، گزارش تصویربرداری (ترجیحاً تصاویر DICOM)، نمونه‌برداری اگر انجام شده، آزمایش خون اخیر و فهرست تاریخ‌دار درمان‌های قبلی."),
                ("بررسی اولیه رایگان است؟", "بله. بررسی از راه دور پرونده رایگان است و شما را به چیزی متعهد نمی‌کند."),
            ]),
            ("گزارش‌ها و برنامه", [
                ("برنامه کی می‌رسد؟", "معمولاً ظرف ۲۴ تا ۴۸ ساعت پس از کامل شدن پرونده. پرونده‌های پیچیده ممکن است بیشتر طول بکشد."),
                ("چه کسی پرونده را می‌خواند؟", "پزشکان تخصص مربوط، و در موارد پیچیده چند تخصص."),
                ("برنامه قطعی است؟", "این یک برنامهٔ پیشنهادی است. پس از ارزیابی هنگام ورود ممکن است تغییر کند؛ هر تغییر پیش از شروع توضیح داده می‌شود."),
            ]),
            ("هزینه و بیمه", [
                ("هزینهٔ درمان چقدر است؟", "هزینه پس از بررسی گزارش پزشکی، برای هر پرونده جداگانه برآورد می‌شود."),
                ("با بیمه‌های بین‌المللی کار می‌کنید؟", "در بسیاری موارد، با تأیید قبلی یا صورتحساب مستقیم."),
            ]),
            ("سفر و اقامت", [
                ("برای ویزا و اقامت کمک می‌کنید؟", "بله. نامهٔ دعوت پزشکی، استقبال در فرودگاه، انتقال و اقامت برای شما و همراه."),
                ("مترجم هست؟", "بله، شبانه‌روزی."),
            ]),
            ("در طول درمان", [
                ("در بیمارستان چه کسی با من است؟", "هماهنگ‌کننده و در صورت نیاز مترجم؛ همراه طبق مقررات بیمارستان می‌تواند بماند."),
                ("اگر لازم باشد بیشتر بمانم؟", "فوری می‌گوییم و برای تمدید اقامت و ویزا کمک می‌کنیم."),
            ]),
            ("پس از بازگشت", [
                ("پیگیری چگونه است؟", "خلاصهٔ ترخیص مفصل، پیگیری از راه دور و تماس با پزشک محل زندگی شما."),
            ]),
            ("انکولوژی و CAR-T", [
                ("درمان CAR-T در بیمارستان دانشگاه بیرونی در دسترس است؟", "بله. CAR-T برای بیماران واجد شرایط در دسترس است. تیم خون و پیوند پس از بررسی پرونده تصمیم می‌گیرد؛ هر بیماری نامزد نیست و نتیجه‌ای تضمین نمی‌شود. " + _cart("fa", "بخوانید: CAR-T در ترکیه، پرسش‌های شما")),
                ("CAR-T چیست؟", "سلول‌های T خون شما در آزمایشگاه طوری تغییر می‌کنند که هدفی روی سلول‌های سرطانی (مانند CD19) را بشناسند و در یک انفوزیون برگردانده می‌شوند. ممکن است در برخی سرطان‌های پیشرفتهٔ خون کمک کند، اما برای همه نیست. (منبع: NCI)"),
                ("آیا CAR-T به معنای درمان کامل است؟", "درمان کامل را نمی‌توان وعده داد. برخی بیماران بهبودی طولانی دارند؛ برخی پاسخ نمی‌دهند یا بیماری برمی‌گردد."),
                ("چه کسی می‌تواند نامزد باشد؟", "معمولاً کسی که بیماری‌اش برگشته یا به درمان استاندارد پاسخ نداده است. تیم نوع بیماری و هدف، سلامت عمومی، قلب، کلیه، کبد و ریه را می‌سنجد. تصمیم نهایی با تیم خون و پیوند بیرونی است."),
                ("برای بررسی از راه دور چه مدارکی لازم است؟", "نمونه‌برداری با رنگ‌آمیزی ایمنی (مثلاً CD19)، گزارش PET-CT، درمان‌های قبلی با تاریخ، آزمایش خون کامل اخیر و گزارش تازه. هماهنگ‌کننده می‌گوید اگر تیم چیز دیگری بخواهد."),
                ("مراحل چیست؟", "ارزیابی، سپس جمع‌آوری سلول، ساخت، گاهی درمان پل، شیمی‌درمانی آماده‌سازی، انفوزیون (معمولاً کمتر از ۳۰ دقیقه)، سپس پایش نزدیک و پیگیری بلندمدت."),
                ("ساخت چقدر طول می‌کشد؟", "معمولاً حدود ۳ تا ۵ هفته از جمع‌آوری تا انفوزیون (NCI). تیم زمان مورد انتظار پروندهٔ شما را می‌گوید."),
                ("عارضه‌های اصلی کدام‌اند؟", "سندرم آزادسازی سایتوکاین (تب، فشار پایین، دشواری تنفس)، سمیت عصبی (گیجی، دشواری گفتار)، افت شمارش خون و خطر عفونت؛ گاهی وضعیت جدی است."),
                ("پس از انفوزیون چقدر باید نزدیک بیمارستان بمانم؟", "در برخی کشورها استاندارد دست‌کم دو هفته نزدیک یک مرکز تخصصی است؛ بسیاری از مراکز از بیماران بین‌المللی می‌خواهند بیشتر بمانند. در بیرونی تیم پیش از سفر مدت پروندهٔ شما را تعیین می‌کند."),
                ("همراه لازم است؟", "معمولاً بله: یک بزرگسال که هفته‌های اول شبانه‌روز در دسترس باشد. هماهنگ‌کننده ترتیب کار را توضیح می‌دهد."),
                ("هزینه چقدر است؟", "پس از بررسی گزارش، هزینه برای هر پرونده جداست. برآورد کتبی بخواهید که بنویسد چه چیزهایی شامل است، از جمله عوارض و مراقبت ویژه."),
                ("پس از بازگشت پیگیری چگونه است؟", "آزمایش خون منظم، ایمونوگلوبولین، تصویربرداری و تماس مرکز با پزشک محل شما؛ پیگیری بلندمدت توصیه می‌شود. تیم بیرونی برنامه را با شما و پزشکتان هماهنگ می‌کند."),
                ("داروی تأییدشده یا کارآزمایی بالینی؟", "محصول تأییدشده را یک نهاد ناظر برای کاربرد مشخص بررسی کرده است. کارآزمایی یک درمان یا کاربرد تازه را می‌آزماید و نتیجه کمتر قطعی است. همیشه شمارهٔ ثبت کارآزمایی را بخواهید."),
            ]),
            ("حریم خصوصی", [
                ("گزارش‌های من کجا نگهداری می‌شود؟", "گزارش‌هایی که با واتساپ یا ایمیل می‌فرستید را تیم بیماران بین‌المللی رسیدگی می‌کند و فقط با تیم پزشکی که پرونده را بررسی می‌کند در میان می‌گذارد."),
                ("می‌توانم حذف داده‌ها را بخواهم؟", "بله، در چارچوب حقوق شما در قانون داده‌های شخصی KVKK (مادهٔ ۱۱)."),
            ]),
        ],
    },
}
