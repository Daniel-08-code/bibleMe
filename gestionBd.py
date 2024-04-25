import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
    
requete = """INSERT INTO questionsReponses (question, choix1, choix2, choix3, choix4, reponse) VALUES
('Quel était le nom de la femme qui a tenté Jésus dans le désert ?', 'Salomé', 'Marie-Madeleine', 'Marthe', 'Lucrèce', 2),
('Qui a été surnommé le "Fils du Tonnerre" par Jésus ?', 'Jean', 'Jacques', 'André', 'Pierre', 2),
('Quel était le nom du prêtre qui a béni Jésus lorsqu''il était bébé dans le temple ?', 'Siméon', 'Caïphe', 'Héli', 'Abiathar', 1),
('Quelle était la profession de Zachee avant de devenir disciple de Jésus ?', 'Collecteur d''impôts', 'Pêcheur', 'Couturier', 'Forgeron', 1),
('Qui était l''épouse de David ?', 'Mical', 'Abigaïl', 'Bathschéba', 'Anne', 3),
('Combien de disciples Jésus avait-il ?', '12', '10', '20', '15', 1),
('Qui a construit l''arche ?', 'Noé', 'Abraham', 'Moïse', 'David', 1),
('Quel est le dernier livre du Nouveau Testament ?', 'Apocalypse', 'Épître aux Hébreux', 'Évangile selon Jean', 'Épître de Jude', 1),
('Qui a marché sur l''eau avec Jésus ?', 'Pierre', 'André', 'Jean', 'Philippe', 1),
('Quel est le nom du père de Moïse ?', 'Amram', 'Aaron', 'Jéthro', 'Pharaon', 1),
('Quel était le nom de la femme de Moïse ?', 'Tsippora', 'Sara', 'Rébecca', 'Ruth', 1),
('Qui a été vendu par ses frères comme esclave en Égypte ?', 'Joseph', 'Jacob', 'Benjamin', 'Ruben', 1),
('Qui a combattu Goliath avec une fronde ?', 'David', 'Saül', 'Samson', 'Jonathan', 1),
('Quel était le métier de Jésus avant de commencer son ministère ?', 'Charpentier', 'Pêcheur', 'Tisserand', 'Forgeron', 1),
('Qui a été jeté dans la fosse aux lions ?', 'Daniel', 'David', 'Joseph', 'Moïse', 1),
('Qui a été choisi pour succéder à Moïse comme chef du peuple d''Israël ?', 'Josué', 'Caleb', 'Aaron', 'Gédéon', 1),
('Combien d''enfants Abraham a-t-il eu ?', '8', '2', '12', '6', 1),
('Qui a reçu la promesse de Dieu d''avoir un fils dans sa vieillesse ?', 'Sara', 'Rebecca', 'Rachel', 'Anne', 1),
('Qui a écrit le livre des Lamentations ?', 'Jérémie', 'Ézéchiel', 'Daniel', 'Amos', 1),
('Qui a été le roi d''Israël après David ?', 'Salomon', 'Saül', 'Jéroboam', 'Roboam', 1);
"""

cur.execute(requete)

conn.commit()
conn.close()