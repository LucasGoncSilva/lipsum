banks: list[str] = [
    ('banco-do-brasil--', 'Banco do Brasil'),
    ('original--', 'Banco Original'),
    ('bradesco--', 'Bradesco'),
    ('caixa--', 'Caixa'),
    ('itau--', 'Itaú'),
    ('next--', 'Next'),
    ('nubank--', 'Nubank'),
    ('pao-de-acucar--', 'Pão de Açúcar'),
    ('pagseguro--', 'PagSeguro'),
    ('paypal--', 'PayPal'),
    ('santander--', 'Santander'),
    ('ticket--', 'Ticket'),
]

brands: list[str] = [
    ('american-express--', 'American Express'),
    ('diners-club-international--', 'Diners Club International'),
    ('elo--', 'Elo'),
    ('hipercard--', 'Hipercard'),
    ('mastercard--', 'Mastercard'),
    ('visa--', 'Visa'),    
]

cards_types: list[str] = [
    ('deb', 'Débito'),
    ('cred', 'Crédito'),
    ('pre', 'Pré-pago'),
    ('co', 'Co-branded'),
]


services: list[str] = [
    ('aws--', 'AWS'),
    ('adobe--', 'Adobe'),
    ('airbnb--', 'Airbnb'),
    ('amazon--', 'Amazon'),
    ('prime-video--', 'Amazon Prime Video'),
    ('apple--', 'Apple'),
    ('booking--', 'Booking'),
    ('deezer--', 'Deezer'),
    ('discord--', 'Discord'),
    ('disney+--', 'Disney+'),
    ('epic-games--', 'Epic Games'),
    ('facebook--', 'Facebook'),
    ('github--', 'Github'),
    ('google--', 'Google'),
    ('gov-br--', 'Gov BR'),
    ('heroku--', 'Heroku'),
    ('instagram--', 'Instagram'),
    ('kayak--', 'Kayak'),
    ('linkedin--', 'LinkedIn'),
    ('magalu--', 'Magazine Luiza'),
    ('mercado-livre--', 'Mercado Livre'),
    ('netflix--', 'Netflix'),
    ('notion--', 'Notion'),
    ('nu-invest--', 'Nu Invest'),
    ('outlook--', 'Outlook'),
    ('pinterest--', 'Pinterest'),
    ('reddit--', 'Reddit'),
    ('spotify--', 'Spotify'),
    ('steam--', 'Steam'),
    ('stripe--', 'Stripe'),
    ('submarino--', 'Submarino'),
    ('ticket--', 'Ticket'),
    ('trello--', 'Trello'),
    ('trip-advisor--', 'Trip Advisor'),
    ('twitch--', 'Twitch'),
    ('twitter--', 'Twitter'),
    ('vercel--', 'Vercel'),
    ('wordpress--', 'Wordpress'),
    ('yahoo--', 'Yahoo'),
    ('atari--', 'Atari'),
    ('blizzard--', 'Blizzard Entertainment'),
    ('lg--', 'LG'),
    ('motorola--', 'Motorola'),
    ('nintendo--', 'Nintendo'),
    ('playstation--', 'PlayStation'),
    ('riot-games--', 'Riot Games'),
    ('samsung--', 'Samsung'),
    ('skype--', 'Skype'),
    ('slack--', 'Slack'),
    ('supercell--', 'Supercell'),
    ('wargaming--', 'Wargaming'),
    ('xbox--', 'Xbox'),
] + banks + brands


cards_banks = sorted(set(banks), key=lambda x: x[1])
cards_brands = sorted(set(brands), key=lambda x: x[1])
credentials_services = sorted(set(services), key=lambda x: x[1])

cards_banks.insert(0, ('nao-listado--', 'NÃO LISTADO'))
cards_brands.insert(0, ('nao-listado--', 'NÃO LISTADO'))
credentials_services.insert(0, ('nao-listado--', 'NÃO LISTADO'))
