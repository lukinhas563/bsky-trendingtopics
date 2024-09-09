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
    "quinta-feira", "sexta-feira", "semana", "oi", "dar", "merda", "fuder", "fude",
    "viu", "tive",
    
    # Interjeições e palavras irrelevantes
    "ai", "ops", "ufa", "eh", "oh", "hã", "poxa", "xi", "uau", "glub", "k", "kk", 
    "kkk", "blo", "yay", "whoa", "ouch", "wow", "meh", "hey", "hmm", "lol", "lmao",
    "pqp", "aju", "ha", "ja", "huh", "ownn"
}