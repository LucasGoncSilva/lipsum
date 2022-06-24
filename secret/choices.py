banks: list[str] = [
    ('banco-do-brasil-', 'Banco do Brasil'),
    ('original-', 'Banco Original'),
    ('bradesco-', 'Bradesco'),
    ('caixa-', 'Caixa'),
    ('itau-', 'Itaú'),
    ('next-', 'Next'),
    ('nubank-', 'Nubank'),
    ('pao-de-acucar-', 'Pão de Açúcar'),
    ('pagseguro-', 'PagSeguro'),
    ('paypal-', 'PayPal'),
    ('santander-', 'Santander'),
    ('ticket-', 'Ticket'),
]

brands: list[str] = [
    ('american-express-', 'American Express'),
    ('diners-club-international-', 'Diners Club International'),
    ('elo-', 'Elo'),
    ('hipercard-', 'Hipercard'),
    ('mastercard-', 'Mastercard'),
    ('visa-', 'Visa'),    
]

cards_types: list[str] = [
    ('deb', 'Débito'),
    ('cred', 'Crédito'),
    ('pre', 'Pré-pago'),
    ('co', 'Co-branded'),
]


services: list[str] = [
    ('aws-', 'AWS'),
    ('adobe-', 'Adobe'),
    ('airbnb-', 'Airbnb'),
    ('amazon-', 'Amazon'),
    ('prime-video-', 'Amazon Prime Video'),
    ('american-express-', 'American Express'),
    ('apple-', 'Apple'),
    ('banco-do-brasil-', 'Banco do Brasil'),
    ('booking-', 'Booking'),
    ('bradesco-', 'Bradesco'),
    ('caixa-', 'Caixa'),
    ('deezer-', 'Deezer'),
    ('diners-club-international-', 'Diners Club International'),
    ('discord-', 'Discord'),
    ('disney+-', 'Disney+'),
    ('elo-', 'Elo'),
    ('epic-games-', 'Epic Games'),
    ('facebook-', 'Facebook'),
    ('github-', 'Github'),
    ('google-', 'Google'),
    ('gov-br-', 'Gov BR'),
    ('heroku-', 'Heroku'),
    ('hipercard-', 'Hipercard'),
    ('instagram-', 'Instagram'),
    ('itau-', 'Itaú'),
    ('kayak-', 'Kayak'),
    ('linkedin-', 'LinkedIn'),
    ('magalu-', 'Magazine Luiza'),
    ('mastercard-', 'Mastercard'),
    ('mercado-livre-', 'Mercado Livre'),
    ('netflix-', 'Netflix'),
    ('next-', 'Next'),
    ('notion-', 'Notion'),
    ('nu-invest-', 'Nu Invest'),
    ('nubank-', 'Nubank'),
    ('outlook-', 'Outlook'),
    ('paypal-', 'PayPal'),
    ('pinterest-', 'Pinterest'),
    ('pao-de-acucar-', 'Pão de Açúcar'),
    ('reddit-', 'Reddit'),
    ('santander-', 'Santander'),
    ('spotify-', 'Spotify'),
    ('steam-', 'Steam'),
    ('stripe-', 'Stripe'),
    ('submarino-', 'Submarino'),
    ('ticket-', 'Ticket'),
    ('trello-', 'Trello'),
    ('trip-advisor-', 'Trip Advisor'),
    ('twitch-', 'Twitch'),
    ('twitter-', 'Twitter'),
    ('vercel-', 'Vercel'),
    ('visa-', 'Visa'),
    ('wordpress-', 'Wordpress'),
    ('yahoo-', 'Yahoo'),
] + banks + brands

# TODO: add default/other services
# TODO: change services from 'xxxx-' to 'xxxx--' and update model's is_valid

cards_banks = sorted(set(banks), key=lambda x: x[1])
cards_brands = sorted(set(brands), key=lambda x: x[1])
credentials_services = sorted(set(services), key=lambda x: x[1])
