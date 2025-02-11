import pandas as pd

#lista de perguntas
questions = [
    ["Em qual ano ocorreu a primeira aparição do Snoopy?", "1999", "1975", "1950", "1962", 3],
    ["Originalmente, qual seria o nome do Snoopy?", "Sniffy", "Scott", "Mickey", "Spike", 1], 
    ["Quem é o criador dos Peanuts?", "Joe Cool", "Paul Clifford", "Charles M. Schulz", "Walter Disney", 3],
    ["Qual é a cor da casa de cachorro do Snoopy?", "Verde", "Amarelo", "Vermelho", "Azul", 3], 
    ["Qual é a raça do nosso querido Snoopy?", "Salsicha", "Beagle", "Pinscher", "Border Collie", 2], 
    ["Quem é o dono do Snoopy?", "Charlie Brown", "Lucy", "Walter", "Sofia", 1], 
    ["Snoopy tem um melhor amigo da cor amarela, qual é seu nome?", "Bob", "Schroeder", "Sam", "Woodstock", 4], 
    ["Qual personagem da turma dos Peanuts toca piano?", "Schroeder", "Sally", "Marcie", "Pig-pen", 1],
    ["Como é chamada a casa do Snoopy onde ele imagina ser um aviador?", "Submarino", "Casa de cachorro", "Avião", "Carro", 2]
    
]

#dataframe
df = pd.DataFrame(questions, columns= ["Questions", "Option01", "Option02", "Option03", "Option4", "Answers"])

df.to_excel("questions.xlsx", index=False)

print("Perguntas inseridas com sucesso!")