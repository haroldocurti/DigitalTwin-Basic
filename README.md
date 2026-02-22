DigitalTwin Basic (v0.1)
Um emulador de sensores IoT focado em modelagem física e comportamento de contexto.

🇧🇷 Português
Conceito: O que é um Gêmeo Digital?
Um Gêmeo Digital (Digital Twin) não é apenas uma simulação estática; é uma réplica virtual dinâmica de um objeto ou sistema físico. O DigitalTwin Basic serve como a unidade fundamental desse conceito, fornecendo um modelo que respeita as leis da física (inércia e sazonalidade) para que sistemas de controle e automação possam ser testados de forma realista antes da implementação no hardware real.

Sobre o Projeto
Este projeto nasceu como uma ferramenta pedagógica para alunos de Internet das Coisas (IoT). Ele permite treinar lógica de monitoramento e integração com plataformas como Home Assistant, fornecendo dados que mimetizam a "sujeira" e o comportamento do mundo real.

Nota da Release v0.1: Esta versão foca exclusivamente na física do sensor e do ambiente. O projeto ainda não possui um módulo de comunicação de rede (MQTT). O objetivo atual é validar o comportamento térmico e a geração de dados.

Sistema de Ambiente (Env_Model)
O ambiente define a verdade teórica.

Modelagem Climática: Utilizamos funções senoidais para simular o ciclo circadiano, onde a temperatura flui naturalmente conforme a estação do ano (Season).

Deslocamento de Fase: Mimica o atraso térmico real (o pico de calor ocorre após o sol atingir o topo).

Correlação Física: A umidade é atrelada à temperatura, garantindo dados coerentes (ex: a umidade cai quando a temperatura sobe).

Sistema de Sensor (Dht22)
O sensor emula as limitações do hardware físico.

Inércia Térmica (Relaxação): O sensor não lê o valor do ambiente instantaneamente; ele simula o tempo de resposta físico para aquecer ou esfriar.

Ruído Gaussiano: Adiciona micro-variações aleatórias para simular interferências eletrônicas reais.

Saída Binária: Suporte a formato binário (16-bit Big-Endian), permitindo praticar a decodificação de payloads brutos.

🇺🇸 English
Concept: What is a Digital Twin?
A Digital Twin is more than a static simulation; it is a dynamic virtual replica of a physical object. DigitalTwin Basic provides the fundamental building blocks of this concept, offering a model that respects physical laws (inertia and seasonality) so that automation systems can be realistically tested.

About the Project
Designed for Internet of Things (IoT) students, this project provides an emulator to practice monitoring logic and integrations (like Home Assistant), offering data that mimics the "noise" and behavior of the real world.

Release v0.1 Note: This version focuses strictly on sensor and environment physics. The project does not yet include a network communication module (MQTT).

Environment System (Env_Model)
Climate Modeling: Uses sine waves to model circadian cycles based on the Season.

Phase Shift: Mimics real-world thermal lag.

Physical Correlation: Humidity is tied to temperature for realistic data behavior.

Sensor System (Dht22)
Thermal Inertia (Relaxation): Simulates physical response time through a relaxation factor.

Gaussian Noise: Adds realistic micro-variations to readings.

Binary Output: Supports 16-bit Big-Endian binary format for raw data practice.

Roadmap
[ ] v0.2: Implementação do módulo MQTT (Publicação de dados).

[ ] v0.3: Sistema de Plugins para novos sensores (DHT11, DS18B20, Solo).

[ ] v1.0: Interface Gráfica (GUI) para controle de estações e sensores.

Estrutura Técnica / Technical Structure
Season: Parâmetros climáticos imutáveis. / Immutable climate parameters.

Env_Model: O motor de contexto (A "Verdade"). / The context engine (The "Truth").

Dht22: O hardware emulado (A "Percepção"). / The emulated hardware (The "Perception").