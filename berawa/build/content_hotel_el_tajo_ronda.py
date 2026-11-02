# Contenido de la demo Hotel El Tajo (Ronda) (es/en/fr/de). Hechos de hoteleltajo.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Doble Superior y Deluxe','Básica, individual y doble de dos camas','Triple familiar y cuádruple'],'en':['Superior and Deluxe Double','Basic, single and twin','Family triple and quadruple'],'fr':['Double Supérieure et Deluxe','Basique, individuelle et lits jumeaux','Triple familiale et quadruple'],'de':['Doppelzimmer Superior und Deluxe','Basic, Einzel- und Zweibettzimmer','Familien-Dreibett und Vierbett']}
RD={
'es':['Reformadas en 2016, la mayoría con cama extragrande de 1,80 m. La Deluxe tiene 30 m², sillones y minibar.','La Básica con cama de 1,35 m, la Individual con cama de 1,05 m y la doble con dos camas individuales.','La triple familiar para 2 adultos y 1 niño; la cuádruple son dos dobles conectadas por una puerta interior.'],
'en':['Renovated in 2016, most with an extra-large 1.80 m bed. The Deluxe has 30 m², armchairs and a minibar.','The Basic with a 1.35 m bed, the Single with a 1.05 m bed and the twin with two single beds.','The family triple for 2 adults and 1 child; the quadruple is two doubles connected by an inner door.'],
'fr':['Rénovées en 2016, la plupart avec un très grand lit de 1,80 m. La Deluxe fait 30 m², avec fauteuils et minibar.','La Basique avec lit de 1,35 m, l’Individuelle avec lit de 1,05 m et la double à deux lits simples.','La triple familiale pour 2 adultes et 1 enfant ; la quadruple, deux doubles reliées par une porte intérieure.'],
'de':['2016 renoviert, meist mit extragroßem 1,80-m-Bett. Das Deluxe hat 30 m², Sessel und Minibar.','Das Basic mit 1,35-m-Bett, das Einzelzimmer mit 1,05-m-Bett und das Zweibettzimmer mit zwei Einzelbetten.','Das Familien-Dreibettzimmer für 2 Erwachsene und 1 Kind; das Vierbettzimmer sind zwei durch eine Innentür verbundene Doppelzimmer.']}
ART={
'hero':('hills',1411,['#2b2016','#b0703c','#e9d4b4','#7a5a3e','#4f3a28','#21180f']),
'intro':('arches',1412,['#f5eee4','#fbf7f1','#8a4a22','#655447','#33251b']),
'r1':('columns',1421,['#f5eee4','#fbf7f1','#8a4a22','#655447','#33251b']),
'r2':('skyline',1422,['#efe7dc','#e3c8a2','#8a4a22','#655447','#33251b']),
'r3':('arches',1423,['#2b2016','#c4844c','#f1dfc4','#86603f','#57402b','#21180f']),
'g1':('hills',1431,['#eef1ea','#dce6d3','#9fb38a','#7c8a6c','#5a654d','#394030']),
'g2':('waves',1432,['#18303d','#5f93a8','#d9ebf1','#4f6d7a','#33505d','#10212a']),
'g3':('columns',1433,['#f5eee4','#fbf7f1','#8a4a22','#655447','#33251b']),
'g4':('skyline',1434,['#2b2016','#c4844c','#f1dfc4','#86603f','#57402b','#21180f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel & Spa El Tajo · Hotel en el centro de Ronda',see_rooms='Ver habitaciones',hero_k='Ronda · Calle Cruz Verde, 7',hero_t='Tu puerta al alma de Ronda',hero_s='A unos pasos de la Calle La Bola y del Puente Nuevo, con spa, solárium y parking propio.',
 intro_t='Encanto andaluz y confort moderno',intro_p1='Un hotel totalmente renovado con 54 habitaciones, Spa & Solárium, gimnasio y parking privado con reserva previa, uno de los pocos del centro.',
 intro_p2='Su equipo está disponible las 24 horas para ayudarte a descubrir Ronda, los Pueblos Blancos y el Caminito del Rey.',
 stats=['54 habitaciones','Recepción 24 h','Spa y solárium','Parking privado'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Todas con aire acondicionado y calefacción, TV, escritorio, caja fuerte, wifi gratis y baño privado con secador.',
 svcs=['Spa con piscina climatizada (solo adultos)','Solárium en la azotea','Gimnasio','Desayuno buffet, también sin gluten bajo petición','Parking privado con reserva previa','Bicicletas gratuitas según disponibilidad'],
 loc_p='Calle Cruz Verde, 7 · 29400 Ronda (Málaga). Teléfono: 952 87 40 40. Correo: reservas@hoteleltajo.com.',
 chips=['¿Qué habitaciones tenéis?','¿Tenéis parking?','¿Cómo es el spa?','¿Cómo reservo?']),
'en':dict(title='Hotel & Spa El Tajo · Hotel in the centre of Ronda',see_rooms='See rooms',hero_k='Ronda · Calle Cruz Verde, 7',hero_t='Your gateway to the soul of Ronda',hero_s='A few steps from Calle La Bola and the Puente Nuevo, with spa, solarium and private parking.',
 intro_t='Andalusian charm and modern comfort',intro_p1='A fully renovated hotel with 54 rooms, Spa & Solarium, gym and private parking on prior booking, one of the few in the centre.',
 intro_p2='The team is available 24 hours a day to help you discover Ronda, the White Villages and the Caminito del Rey.',
 stats=['54 rooms','24-hour reception','Spa and solarium','Private parking'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='All with air conditioning and heating, TV, desk, safe, free wifi and private bathroom with hairdryer.',
 svcs=['Spa with heated pool (adults only)','Rooftop solarium','Gym','Buffet breakfast, gluten-free on request','Private parking on prior booking','Free bikes subject to availability'],
 loc_p='Calle Cruz Verde, 7 · 29400 Ronda (Málaga). Phone: +34 952 87 40 40. Email: reservas@hoteleltajo.com.',
 chips=['Which rooms do you have?','Do you have parking?','What is the spa like?','How do I book?']),
'fr':dict(title='Hotel & Spa El Tajo · Hôtel au centre de Ronda',see_rooms='Voir les chambres',hero_k='Ronda · Calle Cruz Verde, 7',hero_t='Votre porte vers l’âme de Ronda',hero_s='À quelques pas de la Calle La Bola et du Puente Nuevo, avec spa, solarium et parking privé.',
 intro_t='Charme andalou et confort moderne',intro_p1='Un hôtel entièrement rénové de 54 chambres, avec Spa & Solarium, salle de sport et parking privé sur réservation, l’un des rares du centre.',
 intro_p2='L’équipe est disponible 24 h/24 pour vous aider à découvrir Ronda, les Villages blancs et le Caminito del Rey.',
 stats=['54 chambres','Réception 24 h/24','Spa et solarium','Parking privé'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Toutes avec climatisation et chauffage, TV, bureau, coffre-fort, wifi gratuit et salle de bains privée avec sèche-cheveux.',
 svcs=['Spa avec piscine chauffée (adultes uniquement)','Solarium sur le toit','Salle de sport','Petit-déjeuner buffet, sans gluten sur demande','Parking privé sur réservation','Vélos gratuits selon disponibilité'],
 loc_p='Calle Cruz Verde, 7 · 29400 Ronda (Malaga). Téléphone : +34 952 87 40 40. E-mail : reservas@hoteleltajo.com.',
 chips=['Quelles chambres avez-vous ?','Avez-vous un parking ?','Comment est le spa ?','Comment réserver ?']),
'de':dict(title='Hotel & Spa El Tajo · Hotel im Zentrum von Ronda',see_rooms='Zimmer ansehen',hero_k='Ronda · Calle Cruz Verde, 7',hero_t='Ihr Tor zur Seele von Ronda',hero_s='Wenige Schritte von der Calle La Bola und der Puente Nuevo, mit Spa, Solarium und Privatparkplatz.',
 intro_t='Andalusischer Charme und moderner Komfort',intro_p1='Ein komplett renoviertes Hotel mit 54 Zimmern, Spa & Solarium, Fitnessraum und Privatparkplatz nach Voranmeldung, einer der wenigen im Zentrum.',
 intro_p2='Das Team ist rund um die Uhr für Sie da und hilft Ihnen, Ronda, die Weißen Dörfer und den Caminito del Rey zu entdecken.',
 stats=['54 Zimmer','Rezeption rund um die Uhr','Spa und Solarium','Privatparkplatz'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Alle mit Klimaanlage und Heizung, TV, Schreibtisch, Safe, kostenlosem WLAN und eigenem Bad mit Föhn.',
 svcs=['Spa mit beheiztem Pool (nur Erwachsene)','Solarium auf dem Dach','Fitnessraum','Frühstücksbuffet, glutenfrei auf Anfrage','Privatparkplatz nach Voranmeldung','Kostenlose Fahrräder je nach Verfügbarkeit'],
 loc_p='Calle Cruz Verde, 7 · 29400 Ronda (Málaga). Telefon: +34 952 87 40 40. E-Mail: reservas@hoteleltajo.com.',
 chips=['Welche Zimmer gibt es?','Gibt es einen Parkplatz?','Wie ist das Spa?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://www.hoteleltajo.com/es';RN='https://www.hoteleltajo.com/en'
BOOK=dict(mode='engine',url=dict(es=R,en=RN,fr=RN,de=RN))
D=dict(name='Hotel El Tajo',ac='#2b2016',ac2='#8a4a22',ac2_a11y='#7a3f1b',book=BOOK,around=[],foot=FOOT,
 address='Calle Cruz Verde, 7 · 29400 Ronda',phones=['+34 952 87 40 40'],emails=['reservas@hoteleltajo.com'],maps='Hotel El Tajo, Calle Cruz Verde 7, 29400 Ronda',t=T)
META=dict(repo='demo-hotel-el-tajo-ronda',name='Hotel El Tajo',legal_name='Alojamientos Turísticos El Tajo, S.L., CIF B93658730 (aviso legal y pie de su web)',registry_ids=['B93658730'],
 url='https://www.hoteleltajo.com/es',domain='hoteleltajo.com',municipality='Ronda',province='Málaga',sector='hotel con spa en el centro de Ronda',
 read_at='2026-11-02T10:49:00+01:00',created_at='2026-11-02T10:48:00+01:00',built_at='2026-11-02T11:10:00+01:00',audit_date='2026-11-02T10:49:00+01:00',
 rating=dict(value=4.3,coincide=['tel','web'],date='2026-10-30',url='https://www.google.com/maps/search/Hotel+El+Tajo+Ronda?hl=es'),
 book=dict(mode='engine',url=R,note='su web no tiene URL directa de motor: el buscador de reservas (obehotel) va incrustado en la propia pagina (¿Cuándo? ¿Cómo? Buscar) y su boton Reservar no lleva a otra URL; el boton Reservar de la demo lleva a https://www.hoteleltajo.com/es (es) y /en (en/fr/de), HTTP 200 los dos (02/11/2026 10:58).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Tenéis parking?','K03'),('¿Cómo es el spa?','K04'),('¿Hay desayuno?','K05'),('¿Tenéis solárium?','K06'),('¿Dónde estáis?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Hay recepción 24 horas?','K09'),('¿Qué ver en Ronda?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Tenéis bicicletas?','K12'),('¿Cuánto cuesta la noche?',None),('¿Admitís mascotas?',None)],
'en':[('Which rooms do you have?','K01'),('What do the rooms include?','K02'),('Do you have parking?','K03'),('What is the spa like?','K04'),('Is there breakfast?','K05'),('Do you have a solarium?','K06'),('Where are you?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Is reception open 24 hours?','K09'),('What to see in Ronda?','K10'),('What is your phone number?','K11'),('Do you have bikes?','K12'),('How much is a night?',None),('Do you allow pets?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Que comprennent les chambres ?','K02'),('Avez-vous un parking ?','K03'),('Comment est le spa ?','K04'),('Y a-t-il un petit-déjeuner ?','K05'),('Avez-vous un solarium ?','K06'),('Où êtes-vous ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('La réception est-elle ouverte 24 h/24 ?','K09'),('Que voir à Ronda ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Avez-vous des vélos ?','K12'),('Combien coûte la nuit ?',None),('Acceptez-vous les animaux ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was bieten die Zimmer?','K02'),('Gibt es einen Parkplatz?','K03'),('Wie ist das Spa?','K04'),('Gibt es Frühstück?','K05'),('Gibt es ein Solarium?','K06'),('Wo liegt das Hotel?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Ist die Rezeption rund um die Uhr besetzt?','K09'),('Was kann man in Ronda besichtigen?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Gibt es Fahrräder?','K12'),('Was kostet eine Nacht?',None),('Sind Haustiere erlaubt?',None)]}
