stop_words = {
    # Artigos definidos e indefinidos
    "a", "as", "o", "os", "um", "uma", "uns", "umas", "e", "ao", "and", "or", "an",
    "the", "i", "u", "y",
    
    # Preposições e Conjunções
    "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas", 
    "por", "para", "com", "sem", "sobre", "entre", "contra", "até", 
    "após", "antes", "durante", "perante", "atrás", "pra", "mas", "nem",
    "ta", "to", "tô", "pro", "pelo", "estou", "in", "on", "at", "but",
    "this", "that", "those", "these", "for", "of",
    
    # Pronomes
    "eu", "tu", "ele", "ela", "nós", "vós", "eles", "elas", "me", "te", "se", 
    "mim", "ti", "lhe", "nos", "vos", "lhes", "meu", "minha", "meus", "minhas", 
    "teu", "tua", "teus", "tuas", "seu", "sua", "seus", "suas", "dele", "dela", 
    "deles", "delas", "isto", "isso", "aquilo", "este", "esse", "aquele", "esta", 
    "essa", "aquela", "estes", "esses", "aqueles", "estas", "essas", "aquelas", 
    "que", "quem", "onde", "qual", "quando", "quanto", "como", "porque", "porquê", 
    "qualquer", "algum", "alguma", "alguns", "algumas", "você", "nossa", "nosso",
    "our", "mine", "he", "she", "it", "his", "her", "you", "your", "vocês",

    # Verbos auxiliares e comuns
    "é", "foi", "era", "será", "são", "sou", "está", "estava", "estará", "estão", 
    "estar", "tenho", "tinha", "ter", "há", "haver", "vai", "vão", "ser", "pode", 
    "poder", "deve", "dever", "faz", "fazer", "vem", "vir", "bom", "is", "are", "am",
    
    # Advérbios e Partículas
    "não", "sim", "também", "muito", "mais", "menos", "agora", "já", "ainda", 
    "então", "sempre", "nunca", "talvez", "só", "tudo", "todos", "toda", "todo", 
    "nada", "algo", "lá", "cá", "aqui", "ali", "pouco", "demais", "bem", 
    "mal", "assim", "antes", "depois", "aí", "daqui", "dali", "porém", "todavia", 
    "contudo", "entretanto", "ou", "outras", "outro", "seja", "la", "dá", "tambem",
    
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
    "viu", "tive", "msm", "ñ", "obg", "?", "!", "coisas", "quer", "hj", "pessoas",
    "vontade", "preciso", "falar", "ano", "anos", "aguento", "dias", "fui", "pessoa",
    "falando", "tchau", "xau", "adeus", "cair", "viado", "cu", "cú", "caralho", "mo",
    "mó", "ce", "link", "ngm", "ne", "vtmnc", "dnv", "novo", "desse", "sabe", "vezes",
    "cada", "nessa", "logo", "trabalho", "conta", "sendo", "b", "c", "d", "f", "g", "h",
    "j", "k", "l", "m", "p", "r", "s", "t", "v", "w", "x", "z", "meio", "gnt", "casar",
    "que", "oq", "feliz", "fico", "ve", "va", "vi", "vo", "vu", "le", "li", "lo", "lu",
    "ca", "ci", "co", "hora", "volta", "mulher", "dessa", "disso", "menino", "menina",
    "mano", "meno", "pela", "amiga", "amigo", "pelas", "pelos", "lindo", "linda", "música",
    "musica", "mãe", "mae", "mão", "mao", "sinto", "sinta", "fica", "nesse", "cabeça", 
    "quase", "ia", "parece", "foto", "sair", "voltar", "fazendo", "aula", "fosse", "tomar",
    "achei", "comprar", "mto", "primeiro", "agr", "deu", "gosto", "povo", "vamos", "falta",
    "triste", "fala", "ruim", "medo", "final", "ningém", "saber", "igual", "fiz", "fez",
    "passar", "jeito", "fiquei", "usar", "passo", "dois", "mês", "espero", "todas", "juro",
    "outra", "ninguém", "consigo", "maior", "foda", "obrigada", "realmente", "parte", "amigos",
    "pois", "puta", "momento", "posso", "vídeo", "assistir", "chegar", "num", "pensando", "ler",
    "precisa", "nome", "certo", "matar", "primeira", "jogar", "pai", "escola", "galera",
    "lugar", "celular", "existe", "lado", "verdade", "tirar", "problema", "mesma", "filme",
    "vendo", "simplesmente", "grande", "frente", "fim", "seria", "fora", "favor", "outros",
    "duas", "comer", "chorar", "muita", "olha", "tao", "sentindo", "finalmente", "apenas",
    "tivesse", "comigo", "deixar", "indo", "desde", "dor", "causa", "difícil", "legal", "horas",
    "dinheiro", "nova", "bosta", "sono", "disse", "acredito", "acabei", "morrer", "dps",
    "querendo", "dizer", "cima", "nenhum", "dando", "deixa", "horas", "postar", "rede", "ficou",
    "chega", "imagina", "enquanto", "paulo", "trabalhar", "faço", "sério", "começar", "sonho",
    "prova", "dormir", "parar", "viver", "nenhuma", "tanta", "literalmente", "pegar", "gif",
    "cmg", "fumo", "dois", "cinco", "um", "tres", "nois", "pessoal", "entao", "porn",
    
    # Interjeições e palavras irrelevantes
    "ai", "ops", "ufa", "eh", "oh", "hã", "poxa", "xi", "uau", "glub", "k", "kk", 
    "kkk", "blo", "yay", "whoa", "ouch", "wow", "meh", "hey", "hmm", "lol", "lmao",
    "pqp", "aju", "ha", "ja", "huh", "ownn", "aff", "affs", "aka", "shua", "ka", "kkkk",
    "kkkkk", "kkkkkk", "haha", "hahaha", "kakaka", "kkkkkkk", "kkkkkkkk", "uh"
}