from atproto import FirehoseSubscribeReposClient, parse_subscribe_repos_message, models, CAR
from collections import Counter
from datetime import datetime
import re

client = FirehoseSubscribeReposClient()

word_counter = Counter()

stop_words = {
    # Artigos definidos e indefinidos
    "a", "as", "o", "os", "um", "uma", "uns", "umas", "e", "ao", "and", "or", "an",
    "the", "i", "u",
    
    # Preposições e Conjunções
    "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas", 
    "por", "para", "com", "sem", "sobre", "entre", "contra", "até", 
    "após", "antes", "durante", "perante", "atrás", "pra", "mas", "nem",
    "ta", "to", "tô", "pro", "pelo", "estou", "in", "on", "at", "but",
    
    # Pronomes
    "eu", "tu", "ele", "ela", "nós", "vós", "eles", "elas", "me", "te", "se", 
    "mim", "ti", "lhe", "nos", "vos", "lhes", "meu", "minha", "meus", "minhas", 
    "teu", "tua", "teus", "tuas", "seu", "sua", "seus", "suas", "dele", "dela", 
    "deles", "delas", "isto", "isso", "aquilo", "este", "esse", "aquele", "esta", 
    "essa", "aquela", "estes", "esses", "aqueles", "estas", "essas", "aquelas", 
    "que", "quem", "onde", "qual", "quando", "quanto", "como", "porque", "porquê", 
    "qualquer", "algum", "alguma", "alguns", "algumas", "você", "nossa", "nosso",
    "our", "mine", "he", "she", "it", "his", "her", "you", "your",

    # Verbos auxiliares e comuns
    "é", "foi", "era", "será", "são", "sou", "está", "estava", "estará", "estão", 
    "estar", "tenho", "tinha", "ter", "há", "haver", "vai", "vão", "ser", "pode", 
    "poder", "deve", "dever", "faz", "fazer", "vem", "vir", "bom", "is", "are",
    
    # Advérbios e Partículas
    "não", "sim", "também", "muito", "mais", "menos", "agora", "já", "ainda", 
    "então", "sempre", "nunca", "talvez", "só", "tudo", "todos", "toda", "todo", 
    "nada", "algo", "lá", "cá", "aqui", "ali", "pouco", "demais", "bem", 
    "mal", "assim", "antes", "depois", "aí", "daqui", "dali", "porém", "todavia", 
    "contudo", "entretanto", "ou", "outras", "outro", "seja", 
    
    # Gírias e palavras curtas frequentemente usadas
    "né", "tá", "ok", "pq", "vc", "vcs", "tb", "tbm", "blz", "tipo", "ah", "eh", 
    "q", "tem", "gente", "dia", "gore", "really", "n", "vida", "ver", "vou", 
    "to", "mesmo", "nao", "amo", "queria", "acho", "quero", "mundo", "mds", 
    "hoje", "tão", "cara", "sei", "coisa", "casa", "so", "just", "like", "well",
    "mt", "tava", "não", "ir", "p", "amg", "tanto", "cabelo", "amor", "deus",
    "left", "right", "ficar", "cheers", "cheer", "melhor", "pior", "porra", "pariu",
    "odeio", "ontem", "hot", "vez", "nice", "boa", "dia", "noite", "tarde", "show",
    "homem", "alguém", "jogo", "tempo", "domingo", "segunda", "terça", "quarta",
    "quinta", "sexta", "sabado", "segunda-feira", "terça-feira", "quarta-feira",
    "quinta-feira", "sexta-feira", "semana",
    
    # Interjeições e palavras irrelevantes
    "ai", "ops", "ufa", "eh", "oh", "hã", "poxa", "xi", "uau", "glub", "k", "kk", 
    "kkk", "blo", "yay", "whoa", "ouch", "wow", "meh", "hey", "hmm", "lol", "lmao",
    "pqp", "aju", "ha", "ja"
}

def preprocess_text(text):
    """
    Pré-processa o texto removendo pontuações e convertendo para minúsculas.
    """

    text = re.sub(r'[^\w\s#]', '', text)
    text = text.lower()
    return text

def generate_ngrams(words, n):
    """
    Gera n-gramas a partir de uma lista de palavras.
    """
    return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]

def process_post_text(text):
    """
    Processa o texto do post, removendo stop-words e atualizando o contador de palavras.
    """

    words = preprocess_text(text).split()
    filtered_words = [word for word in words if word not in stop_words]
    
    # Atualizar contadores
    word_counter.update(filtered_words)

def on_message_handler(message) -> None:
    commit = parse_subscribe_repos_message(message)

    if not isinstance(commit, models.ComAtprotoSyncSubscribeRepos.Commit):
        return

    if not commit.blocks:
        return

    car = CAR.from_bytes(commit.blocks)

    for cid, block in car.blocks.items():

        try:
            if isinstance(block, dict):
                if '$type' in block:
                    if block['$type'] == 'app.bsky.feed.post':
                        if block.get('langs') and block['langs'][0] == 'pt':
                            print(block['text'])
                            process_post_text(block['text'])

        except Exception as e:
            print(f"Erro ao processar bloco {cid}: {e}")

def display_trending_topics(top_n=5):
    """
    Exibe os trending topics com base no contador de palavras.
    """
    print(f"🔴 posts processados: {word_counter.total()}")
    print("\n🔴 Trending Topics:")
    print(f"🕗 {datetime.now()}")
    for i, (word, count) in enumerate(word_counter.most_common(top_n), start=1):
        print(f"{i}. {word} #{count} posts")

def limited_message_processing(limit=1000):
    message_count = 0

    def handler(message):
        nonlocal message_count

        if word_counter.total() >= limit:
            client.stop()
            display_trending_topics()
            return
        
        on_message_handler(message)
        message_count += 1
           
    return handler

client.start(limited_message_processing(limit=200000))