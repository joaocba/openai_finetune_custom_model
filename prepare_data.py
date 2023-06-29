import json
import openai
import os


# set openai API key
# openai.api_key = ''
# os.environ["OPENAI_API_KEY"] = ''
# in case it is already defined on windows path variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

# add training data using the scheme {"prompt": "<question>", "completion": "<ideal answer>"} per line
training_data = [{"prompt":"O que é a PrimeIT? ->","completion":"A PrimeIT é uma empresa internacional com mais de 16 anos de experiência em serviços de Consultoria Especializada, Nearshore, Gestão de Projecto e Projectos Fechados. Actuamos em 5 sectores principais - IT, Telecom, Energia, Infraestruturas e Marketing Digital - e contamos com uma equipa de mais de 2300 Primers no desenvolvimento de projectos nacionais e internacionais. Com 17 escritórios e presença em mais de 50 cidades em todo o Mundo, a nossa atitude diferenciadora é baseada nos mais elevados padrões de qualidade, o que nos tem permitido um crescimento e sucesso contínuo ao longo dos anos.\n"},
{"prompt":"Como é trabalhar na PrimeIT? ->","completion":"A classificação geral da PrimeIT é de 1.8/5.0, com equilíbrio trabalho/vida pessoal a ser a melhor classificação. No entanto, salário é avaliado como a pior. Para saber em primeira mão como é trabalhar na PrimeIT, lê as reviews detalhadas por cargo, departamento e localização na secção de reviews.\n"},
{"prompt":"Quanto é o salário na PrimeIT? ->","completion":"O salário médio bruto mensal para profissionais de tecnologia na PrimeIT está entre os 1,279€ e 1,479€. Para obteres informações sobre remunerações detalhadas visita a página de salários.\n"},
{"prompt":"Qual é o horário de trabalho na PrimeIT? ->","completion":"95 funcionários relataram o horário de trabalho na PrimeIT ser em média 08:09h por dia.\n"},
{"prompt":"PrimeIT dá feedback das entrevistas de emprego? ->","completion":"28% dos candidatos que participaram em entrevistas na PrimeIT dizem que receberam feedback mais tarde dos recrutadores.\n"},
{"prompt":"Como são as entrevistas na PrimeIT? ->","completion":"237 candidatos na PrimeIT consideraram em média a entrevista fácil em termos de dificuldade atribuindo a pontuação agregada de 1.6/5.0.\n"},
{"prompt":"Qual a taxa de recomendação para se trabalhar na PrimeIT ->","completion":"23%\n"},
{"prompt":"Qual o número de horas trabalhadas em média na PrimeIT ->","completion":"08:09 horas\n"},
{"prompt":"Qual a dificuldade das entrevistas na PrimeIT ->","completion":"1.6/5.0\n"},
{"prompt":"Qual a taxa de feedback das entrevistas na PrimeIT ->","completion":"28%\n"},
{"prompt":"Quanto tempo de Investimento em média por entrevista na PrimeIT ->","completion":"01:03 horas\n"},
{"prompt":"Como é realizado o recrutamento na PrimeIT ->","completion":"Candidatura Direta, Estágio Profissional e Academia de Trainees\n"},
{"prompt":"Quais as áreas de negócio da PrimeIT ->","completion":"Consulting, Insourcing, Nearshoring, Outsourcing, Prime Solutions, Project Management e Specialized Consulting\n"},
{"prompt":"Qual a opinião da comunidade sobre a PrimeIT ->","completion":"36% acha atractiva ou que gostava de ir a uma entrevista, 61% acha pouco selectiva e participou num recrutamento, 58% acha que faz algum spam ou associa a empresa ao spam\n"},
{"prompt":"O que é a Novabase? ->","completion":"A Novabase surge como software-house, especializada no desenvolvimento de soluções à medida. Em 1994 torna-se a primeira empresa no mercado do desenvolvimento de software em Portugal que obteve a norma de certificação do seu processo produtivo pelo IPQ, segundo a NP EN ISO 9001.\n"},
{"prompt":"Como é trabalhar na Novabase? ->","completion":"A classificação geral da Novabase é de 2.3/5.0, com equilíbrio trabalho/vida pessoal a ser a melhor classificação. No entanto, reconhecimento e recompensa é avaliado como a pior. Para saber em primeira mão como é trabalhar na Novabase, lê as reviews detalhadas por cargo, departamento e localização na secção de reviews.\n"},
{"prompt":"Quanto é o salário na Novabase? ->","completion":"O salário médio bruto mensal para profissionais de tecnologia na Novabase está entre os 1,306€ e 1,506€. Para obteres informações sobre remunerações detalhadas visita a página de salários.\n"},
{"prompt":"Qual é o horário de trabalho na Novabase? ->","completion":"97 funcionários relataram o horário de trabalho na Novabase ser em média 08:03h por dia.\n"},
{"prompt":"Novabase dá feedback das entrevistas de emprego? ->","completion":"66% dos candidatos que participaram em entrevistas na Novabase dizem que receberam feedback mais tarde dos recrutadores.\n"},
{"prompt":"Como são as entrevistas na Novabase? ->","completion":"47 candidatos na Novabase consideraram em média a entrevista normal em termos de dificuldade atribuindo a pontuação agregada de 2.1/5.0.\n"},
{"prompt":"Qual a taxa de recomendação para se trabalhar na Novabase ->","completion":"61%\n"},
{"prompt":"Qual o número de horas trabalhadas em média na Novabase ->","completion":"08:03 horas\n"},
{"prompt":"Qual a dificuldade das entrevistas na Novabase ->","completion":"2.1/5.0\n"},
{"prompt":"Qual a taxa de feedback das entrevistas na Novabase ->","completion":"66%\n"},
{"prompt":"Quanto tempo de Investimento em média por entrevista na Novabase ->","completion":"01:46 horas\n"},
{"prompt":"Como é realizado o recrutamento na Novabase ->","completion":"Estágio Profissional, Estágio Curricular e Estágio de Verão\n"},
{"prompt":"Quais as áreas de negócio da Novabase ->","completion":"Energy, Financial Services, Government, Telecommunications e Transports\n"},
{"prompt":"Qual a opinião da comunidade sobre a Novabase ->","completion":"68% acha atractiva ou que gostava de ir a uma entrevista, 50% acha pouco selectiva e participou num recrutamento, 16% acha que faz algum spam ou associa a empresa ao spam\n"},
{"prompt":"O que é a Farfetch? ->","completion":"José Neves lançou a Farfetch em 2008, com tecnologia desenvolvida em Leça do Balio. Com sede em Londres, o site de comércio online de produtos de luxo está avaliado em 894 milhões de euros.\n"},
{"prompt":"Como é trabalhar na Farfetch? ->","completion":"A classificação geral da Farfetch é de 2.6/5.0, com equilíbrio trabalho/vida pessoal a ser a melhor classificação. No entanto, qualidade de gestão é avaliado como a pior. Para saber em primeira mão como é trabalhar na Farfetch, lê as reviews detalhadas por cargo, departamento e localização na secção de reviews.\n"},
{"prompt":"Quanto é o salário na Farfetch? ->","completion":"O salário médio bruto mensal para profissionais de tecnologia na Farfetch está entre os 2,145€ e 2,345€. Para obteres informações sobre remunerações detalhadas visita a página de salários.\n"},
{"prompt":"Qual é o horário de trabalho na Farfetch? ->","completion":"110 funcionários relataram o horário de trabalho na Farfetch ser em média 07:56h por dia.\n"},
{"prompt":"Farfetch dá feedback das entrevistas de emprego? ->","completion":"73% dos candidatos que participaram em entrevistas na Farfetch dizem que receberam feedback mais tarde dos recrutadores.\n"},
{"prompt":"Como são as entrevistas na Farfetch? ->","completion":"88 candidatos na Farfetch consideraram em média a entrevista normal em termos de dificuldade atribuindo a pontuação agregada de 2.5/5.0.\n"},
{"prompt":"Qual a taxa de recomendação para se trabalhar na Farfetch ->","completion":"56%\n"},
{"prompt":"Qual o número de horas trabalhadas em média na Farfetch ->","completion":"07:56 horas\n"},
{"prompt":"Qual a dificuldade das entrevistas na Farfetch ->","completion":"2.5/5.0\n"},
{"prompt":"Qual a taxa de feedback das entrevistas na Farfetch ->","completion":"73%\n"},
{"prompt":"Quanto tempo de Investimento em média por entrevista na Farfetch ->","completion":"02:22 horas\n"},
{"prompt":"Como é realizado o recrutamento na Farfetch ->","completion":"Candidatura Direta, Academia de Trainees, Estágio Profissional, Estágio Curricular e Estágio de Verão\n"},
{"prompt":"Quais as áreas de negócio da Farfetch ->","completion":"Augmented Retail, Designer, Digital, E-commerce, Editorial, Fashion, Luxury, Online Shopping, Retail e Technology\n"},
{"prompt":"Qual a opinião da comunidade sobre a Farfetch ->","completion":"76% acha atractiva ou que gostava de ir a uma entrevista, 40% acha pouco selectiva e participou num recrutamento, 11% acha que faz algum spam ou associa a empresa ao spam\n"},
{"prompt":"O que é a Noesis? ->","completion":"Somos consultora tecnológica internacional e contamos com mil talentos especializados em diferentes tecnologias. Todos os dias, trabalhamos em conjunto para criar soluções inovadoras com impacto na sociedade. Estamos em Portugal, Espanha, Holanda, Brasil, Irlanda e EUA. É na diversidade cultural e de oportunidades que encontramos o estímulo para inovar e nos desafiarmos a ser cada vez melhores.\n"},
{"prompt":"Como é trabalhar na Noesis? ->","completion":"A classificação geral da Noesis é de 2.1/5.0, com equilíbrio trabalho/vida pessoal a ser a melhor classificação. No entanto, salário é avaliado como a pior. Para saber em primeira mão como é trabalhar na Noesis, lê as reviews detalhadas por cargo, departamento e localização na secção de reviews.\n"},
{"prompt":"Quanto é o salário na Noesis? ->","completion":"O salário médio bruto mensal para profissionais de tecnologia na Noesis está entre os 1,181€ e 1,381€. Para obteres informações sobre remunerações detalhadas visita a página de salários.\n"},
{"prompt":"Qual é o horário de trabalho na Noesis? ->","completion":"58 funcionários relataram o horário de trabalho na Noesis ser em média 08:01h por dia.\n"},
{"prompt":"Noesis dá feedback das entrevistas de emprego? ->","completion":"62% dos candidatos que participaram em entrevistas na Noesis dizem que receberam feedback mais tarde dos recrutadores.\n"},
{"prompt":"Como são as entrevistas na Noesis? ->","completion":"35 candidatos na Noesis consideraram em média a entrevista fácil em termos de dificuldade atribuindo a pontuação agregada de 1.5/5.0.\n"},
{"prompt":"Qual a taxa de recomendação para se trabalhar na Noesis ->","completion":"44%\n"},
{"prompt":"Qual o número de horas trabalhadas em média na Noesis ->","completion":"08:01 horas\n"},
{"prompt":"Qual a dificuldade das entrevistas na Noesis ->","completion":"1.5/5.0\n"},
{"prompt":"Qual a taxa de feedback das entrevistas na Noesis ->","completion":"62%\n"},
{"prompt":"Quanto tempo de Investimento em média por entrevista na Noesis ->","completion":"01:05 horas\n"},
{"prompt":"Como é realizado o recrutamento na Noesis ->","completion":"Candidatura Direta\n"},
{"prompt":"Quais as áreas de negócio da Noesis ->","completion":"Agile Solutions, Business Intelligence e Enterprise Resource\n"},
{"prompt":"Qual a opinião da comunidade sobre a Noesis ->","completion":"62% acha atractiva ou que gostava de ir a uma entrevista, 60% acha pouco selectiva e participou num recrutamento, 17% acha que faz algum spam ou associa a empresa ao spam\n"},
{"prompt":"O que é a Adentis Portugal? ->","completion":"A Adentis Portugal é uma consultora tecnológica focada na inovação e especializada no desenvolvimento de projetos em sistemas de informação, com três vertentes de execução: Outsourcing, Customized Solutions e R&D_Lab.\n"},
{"prompt":"Como é trabalhar na Adentis Portugal? ->","completion":"A classificação geral da Adentis Portugal é de 2.3/5.0, com equilíbrio trabalho/vida pessoal a ser a melhor classificação. No entanto, salário é avaliado como a pior. Para saber em primeira mão como é trabalhar na Adentis Portugal, lê as reviews detalhadas por cargo, departamento e localização na secção de reviews.\n"},
{"prompt":"Quanto é o salário na Adentis Portugal? ->","completion":"O salário médio bruto mensal para profissionais de tecnologia na Adentis Portugal está entre os 1,268€ e 1,468€. Para obteres informações sobre remunerações detalhadas visita a página de salários.\n"},
{"prompt":"Qual é o horário de trabalho na Adentis Portugal? ->","completion":"25 funcionários relataram o horário de trabalho na Adentis Portugal ser em média 07:51h por dia.\n"},
{"prompt":"Adentis Portugal dá feedback das entrevistas de emprego? ->","completion":"42% dos candidatos que participaram em entrevistas na Adentis Portugal dizem que receberam feedback mais tarde dos recrutadores.\n"},
{"prompt":"Como são as entrevistas na Adentis Portugal? ->","completion":"80 candidatos na Adentis Portugal consideraram em média a entrevista fácil em termos de dificuldade atribuindo a pontuação agregada de 1.8/5.0.\n"},
{"prompt":"Qual a taxa de recomendação para se trabalhar na Adentis Portugal ->","completion":"72%\n"},
{"prompt":"Qual o número de horas trabalhadas em média na Adentis Portugal ->","completion":"07:51 horas\n"},
{"prompt":"Qual a dificuldade das entrevistas na Adentis Portugal ->","completion":"1.8/5.0\n"},
{"prompt":"Qual a taxa de feedback das entrevistas na Adentis Portugal ->","completion":"42%\n"},
{"prompt":"Quanto tempo de Investimento em média por entrevista na Adentis Portugal ->","completion":"01:05 horas\n"},
{"prompt":"Como é realizado o recrutamento na Adentis Portugal ->","completion":"Candidatura Direta e Estágio Profissional\n"},
{"prompt":"Quais as áreas de negócio da Adentis Portugal ->","completion":"Customized Solutions, Outsourcing, R&D_Lab e Sistemas de Informacao\n"},
{"prompt":"Qual a opinião da comunidade sobre a Adentis Portugal ->","completion":"76% acha atractiva ou que gostava de ir a uma entrevista, 63% acha pouco selectiva e participou num recrutamento, 21% acha que faz algum spam ou associa a empresa ao spam\n"},
{"prompt":"O que é a Softinsa? ->","completion":"A Softinsa, uma subsidiária da IBM, é especialista em serviços de consultoria, gestão e desenvolvimento de aplicações. Com 24 anos de história e experiência no mercado português, conta atualmente com uma equipa de mais de 800 profissionais, distribuídos por Lisboa, pelos Centros de Inovação de Tomar, Viseu, Fundão, Portalegre e Vila Real.\n"},
{"prompt":"Como é trabalhar na Softinsa? ->","completion":"A classificação geral da Softinsa é de 1.9/5.0, com equilíbrio trabalho/vida pessoal a ser a melhor classificação. No entanto, salário é avaliado como a pior. Para saber em primeira mão como é trabalhar na Softinsa, lê as reviews detalhadas por cargo, departamento e localização na secção de reviews.\n"},
{"prompt":"Quanto é o salário na Softinsa? ->","completion":"O salário médio bruto mensal para profissionais de tecnologia na Softinsa está entre os 994€ e 1,194€. Para obteres informações sobre remunerações detalhadas visita a página de salários.\n"},
{"prompt":"Qual é o horário de trabalho na Softinsa? ->","completion":"58 funcionários relataram o horário de trabalho na Softinsa ser em média 08:08h por dia.\n"},
{"prompt":"Softinsa dá feedback das entrevistas de emprego? ->","completion":"63% dos candidatos que participaram em entrevistas na Softinsa dizem que receberam feedback mais tarde dos recrutadores.\n"},
{"prompt":"Como são as entrevistas na Softinsa? ->","completion":"33 candidatos na Softinsa consideraram em média a entrevista fácil em termos de dificuldade atribuindo a pontuação agregada de 1.6/5.0.\n"},
{"prompt":"Qual a taxa de recomendação para se trabalhar na Softinsa ->","completion":"32%\n"},
{"prompt":"Qual o número de horas trabalhadas em média na Softinsa ->","completion":"08:08 horas\n"},
{"prompt":"Qual a dificuldade das entrevistas na Softinsa ->","completion":"1.6/5.0\n"},
{"prompt":"Qual a taxa de feedback das entrevistas na Softinsa ->","completion":"63%\n"},
{"prompt":"Quanto tempo de Investimento em média por entrevista na Softinsa ->","completion":"01:33 horas\n"},
{"prompt":"Como é realizado o recrutamento na Softinsa ->","completion":"Candidatura Direta, Academia de Trainees, Estágio Profissional, Estágio Internacional e Estágio Curricular\n"},
{"prompt":"Quais as áreas de negócio da Softinsa ->","completion":"Application Development, Business Intelligence, Cloud Services, Desenvolvimento Aplicacional, End User Computing, Enterprise Applications, Human Capital, IBM Maximo, Infrastructures, Managed Services, Mobile, Out-Tasking, SAP, Smarter Cities e Testing \n"},
{"prompt":"Qual a opinião da comunidade sobre a Softinsa ->","completion":"61% acha atractiva ou que gostava de ir a uma entrevista, 57% acha pouco selectiva e participou num recrutamento, 21% acha que faz algum spam ou associa a empresa ao spam\n"}]

# set name for output file
file_name = "training_data.jsonl"

with open(file_name, "w") as output_file:
 for entry in training_data:
  json.dump(entry, output_file)
  output_file.write("\n")


## How to run:
# run 'virtualenv env'
# run 'env\Scripts\activate'
# run 'pip install openai==0.25.0'

# run 'python prepare_data.py' to create jsonl file with added data
# after generating output file
# run command 'openai tools fine_tunes.prepare_data -f training_data.jsonl' to normalize the data for proper fine-tune process
# it will generate a new file called 'training_data_prepared.jsonl'


# switch to 'upload_data.py' file or follow steps below to run manually and ignore 'upload_data.py' file


# after preparing data
# run command 'openai --api-key <OPENAI API HERE> api fine_tunes.create -t training_data_prepared.jsonl -m davinci' to initiate the upload and fine-tune process
# this will prompt info regarding fine-tune ID, example -> [2023-03-10 11:42:18] Created fine-tune: ft-F3z6F7gZP2KxkZgJlQEKuX3P
# the "ft-F3z6F7gZP2KxkZgJlQEKuX3P" is the ID for the current fine-tune process
# to follow its status run the command 'openai --api-key <OPENAI API HERE> api fine_tunes.follow -i <FINE-TUNE ID HERE>'
# once its finished it will show a message "Job complete! Status: succeeded" and will show the name of the fine-tune model created
# example: davinci:ft-personal-2023-03-09-23-58-30
# model name can also be listed on openai playground at model selector (https://platform.openai.com/playground)


# switch to 'app.py' file