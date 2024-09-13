from typing import Final
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext, CallbackQueryHandler

TOKEN: Final = "6374678693:AAG_1Mjl2TjUvjS1pIc-DB10jzHw2rzOlHY"
BOT_USERNAME: Final = "@lingualexbot"


print('Starting up bot...')

# Glossary of words and their definitions
word_definitions = {
    "1️⃣ ability / здатність":
    
    """
1️⃣

💫 <b>ability / здатність</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 100 / частота: 78</i>

🇬🇧 <b>ability</b> - the physical or mental power or skill needed to do something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Our brains have mechanisms for acquiring new routines, and part of what makes us, and other creatures successful is the <b>ability</b> to create these habits.</i> <a href="https://www.bbc.com/future/article/20120327-why-do-we-have-superstitions">[04_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>здатність</b> - уміння здійснювати, виконувати, робити що-небудь, поводити себе певним чином. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Наш мозок має механізми для перетворення дій у звичні ритуали, і ця <b>здатність</b> як у людей, так і тварин є надзвичайно важливою в боротьбі за виживання.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-38610222">[04_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣ actually / насправді": 
    
    """
2️⃣

💫 <b>actually / насправді</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 140 / частота: 276</i>

🇬🇧 <b>actually</b> - in fact or really. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>But <b>actually</b>, the biggest advantage of knowing foreign languages is being able to communicate with more people.</i> <a href="https://www.bbc.com/future/article/20181024-the-best-age-to-learn-a-foreign-language">[133_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>насправді</b> - у дійсності; дійсно, справді. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Але <b>насправді</b> найбільша перевага володіння іноземною мовою - це можливість спілкуватися з більшим числом людей.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-45997320">[133_BBC_Future_Corpus_UKR]</a>
    """,

    "3️⃣ add / додавати": 
    
    """
3️⃣

💫 <b>add / додавати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 170 / частота: 203</i>

🇬🇧 <b>add</b> - to put something with something else to increase the number or amount or to improve the whole. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>The only thing left to do was crack a raw egg on top, <b>add</b> a plus-sized dollop of butter, stir it in, and commence eating one of the most delicious things on the planet.</i> <a href="https://www.bbc.com/travel/article/20171120-georgias-addictive-cousin-to-pizza">[80_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>додавати</b> - збільшувати, посилювати, робити відчутним що-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Останній штрих - розбити сире яйце, вилити його на готову страву і <b>додати</b> трохи вершкового масла. Тепер можна починати їсти одну з найсмачніших страв на землі.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-42202640">[80_BBC_Travel_Corpus_UKR]</a>
    """,

    "4️⃣ again / знову": 
    
    """
4️⃣

💫 <b>again / знову</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 109 / частота: 94</i>

🇬🇧 <b>again</b> - one more time. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>She and I had met <b>again</b> after my return from Lapland for a sauna session in the Helsinki neighbourhood of Kallio. If there is any activity that defines what Finns most enjoy about life, it is the sauna.</i> <a href="https://www.bbc.com/travel/article/20180225-the-mysterious-origins-of-finlands-true-name">[63_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>знову</b> - ще раз, ще, удруге; повторно. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Із Крістою ми <b>знову</b> зустрілися після мого повернення з Лапландії і вирішили піти в сауну - найулюбленіше заняття фінів.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-43200728">[63_BBC_Travel_Corpus_UKR]</a>
    """,

    "5️⃣ age / вік": 
    
    """
5️⃣

💫 <b>age / вік</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 154 / частота: 108</i>

🇬🇧 <b>age</b> - the period of time someone has been alive or something has existed. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>This depends a lot on the <b>age</b> of the child, of course. With pre-school children any kind of praise seems to motivate them, but when they’re a bit older subtleties of praise is everything.</i> <a href="https://www.bbc.com/future/article/20140204-is-it-right-to-praise-a-child">[184_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>вік</b> - тривалість життя людини, тварини, рослини. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Багато залежить і від <b>віку</b> дитини. Для дошкільнят будь-яка похвала виявляється важливою, але коли вони стають старшими, великого значення набувають відтінки похвали.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151008_vert_fut_is_it_right_to_praise_a_child_vp">[184_BBC_Future_Corpus_UKR]</a>
    """,

    "6️⃣ ago / тому": 
    
    """
6️⃣

💫 <b>ago / тому</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 102 / частота: 580</i>

🇬🇧 <b>ago</b> - back in time from the present. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Guo started his operation only two years <b>ago</b>, and mines like his have boomed ever since.</i> <a href="https://www.bbc.com/future/article/20160504-we-looked-inside-a-secret-chinese-bitcoin-mine">[99_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>тому</b> - указує на час, що минув від якоїсь дії, події, стану. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Го відкрив "шахту" лише два роки <b>тому</b>, але з того часу цей бізнес почав швидко розвиватися.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/05/160508_vert_fut_we_looked_inside_a_secret_chinese_bitcoin_mine_vp_rl">[99_BBC_Future_Corpus_UKR]</a>
    """,

    "7️⃣ almost / майже": 
    
    """
7️⃣

💫 <b>almost/ майже</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 133 / частота: 202</i>

🇬🇧 <b>almost</b> - nearly. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>He now speaks at least 20 languages fluently, <b>almost</b> all of which were learnt as an adult.</i> <a href="https://www.bbc.com/future/article/20150528-how-to-learn-30-languages">[41_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>майже</b> - так, що трохи не вистачає до чого-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Тепер він вільно говорить щонайменш 20 мовами, <b>майже</b> всі з яких він вивчив вже дорослим.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150804_vert_fut_how_to_learn_30_languages_vp">[41_BBC_Future_Corpus_UKR]</a>
    """,

    "8️⃣ already / вже": 
    
    """
8️⃣

💫 <b>already / вже</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 106 / частота: 342</i>

🇬🇧 <b>already</b> - before the present time. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>However, what chatbots are fully capable of in everyday life is far more interesting. We’re <b>already</b> surrounded by bots capable of tricking us into thinking they are real people, and they don’t enter competitions.</i> <a href="https://www.bbc.com/future/article/20140609-how-online-bots-are-tricking-you">[53_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>вже</b> - указує на остаточне здійснення чи настання дії, явища, ознаки, стану. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Але в повсякденному житті чат-боти вміють робити багато цікавих речей. Ми <b>вже</b> оточені ботами, які змушують нас вірити, що вони реальні люди, і ці боти не беруть участі у змаганнях.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150818_vert_fut_how_online_bots_are_tricking_you_vp">[53_BBC_Future_Corpus_UKR]</a>
    """,

    "9️⃣ also / також": 
    
    """
9️⃣

💫 <b>also / також</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 715 / частота: 729</i>

🇬🇧 <b>also</b> - in addition. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>But it <b>also</b> offers an opportunity to change the way you’re seen by others.</i> <a href="https://www.bbc.com/future/article/20170720-the-hidden-ways-your-language-betrays-your-character">[175_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>також</b> - так само, таким же чином. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Але це <b>також</b> дає можливість справляти на інших людей бажане враження.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-40708690">[175_BBC_Future_Corpus_UKR]</a>
    """,

    "🔟 always / завжди": 
    
    """
🔟

💫 <b>always / завжди</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 159 / частота: 188</i>

🇬🇧 <b>always</b> - every time or all the time. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Unfortunately, it’s not <b>always</b> easy to prune these people from your social network – especially considering the fact that they are often lifelong friendships.</i> <a href="https://www.bbc.com/future/article/20141119-why-you-love-to-hate-some-friends">[82_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>завжди</b> - у будь-який час, повсякчас, постійно. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>На жаль, позбутися таких стосунків не <b>завжди</b> буває легко, особливо коли це стосується дружби всього життя.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151209_vert_fut_why_you_love_to_hate_some_friends_vp">[82_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣1️⃣ animal  / тварина": 
    
    """
1️⃣1️⃣

💫 <b>animal / тварина</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 100 / частота: 102</i>

🇬🇧 <b>animal</b> - something that lives and moves but is not a human, bird, fish, or insect. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Whereas the braver <b>animals</b> may find more mates and eat more food, the shyer individuals, hiding on the side-lines, might avoid attack – both successful evolutionary strategies.</i> <a href="https://www.bbc.com/future/article/20160830-why-we-should-celebrate-shyness">[166_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>тварина</b> - будь-яка істота на відміну від рослини чи людини. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Якщо хоробрі <b>тварини</b> мають більше шансів знайти партнера і здобути їжу, то їх боязкі співбрати, які ведуть більш прихований спосіб життя, зазвичай уникають нападів інших тварин. І те й інше є успішною стратегією виживання.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/09/160902_vert_fut_why_we_should_celebrate_shyness_vp">[166_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣2️⃣ answer / відповідати": 
    
    """
1️⃣2️⃣

💫 <b>answer / відповідати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 125 / частота: 149</i>

🇬🇧 <b>answer</b> - to say, write, or do something as a reaction to a question, letter, etc. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“What’s your secret ingredient?” Almost everyone <b>answered</b>, “Love.”</i> <a href="https://www.bbc.com/travel/article/20171211-who-invented-hummus">[15_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>відповідати</b> - давати комусь відповідь на питання, звертання тощо. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>На запитання про секретний інгредієнт хумусу, всі вони одноголосно <b>відповіли</b>: "Любов".</i> <a href="https://www.bbc.com/ukrainian/vert-tra-42416706">[15_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣3️⃣ appear / з'являтися": 
    
    """
1️⃣3️⃣

💫 <b>appear / з'являтися</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 119 / частота: 66</i>

🇬🇧 <b>appear</b> - to start to be seen or to be present. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>On average, patchy footage <b>appears</b> from about three-and-a-half.</i> <a href="https://www.bbc.com/future/article/20160726-the-mystery-of-why-you-cant-remember-being-a-baby">[165_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>з'являтися</b> - ставати наявним де-небудь; бути в наявності. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>В середньому уривчасті спогади починають <b>з'являтись</b> з трьох з половиною років.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/07/160727_vert_fut_mystery_of_why_you_cant_remember_being_a_baby_vp">[165_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣4️⃣ area / ділянка": 
    
    """
1️⃣4️⃣

💫 <b>area / ділянка</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 137 / частота: 50</i>

🇬🇧 <b>area</b> - a particular part of a place, piece of land, or country. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Different <b>areas</b> of the tongue can taste anything, but although some regions are slightly more sensitive to certain tastes, those differences, in Steven Munger’s words are “minute”.</i> <a href="https://www.bbc.com/future/article/20171012-do-our-tongues-have-different-taste-zones">[14_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>ділянка</b> - частина поверхні, площі чого-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Різні <b>ділянки</b> язика здатні розпізнати всі п'ять смаків. І хоча деякі його частини є трохи більш чутливими до певних смаків, на думку Стівена Мунгера, ця різниця незначна.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-41665560">[14_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣5️⃣ ask / запитати": 
    
    """
1️⃣5️⃣

💫 <b>ask / запитати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 293 / частота: 36</i>

🇬🇧 <b>ask</b> - to put a question to someone, or to request an answer from someone. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>A teenage girl came over to <b>ask</b> where we were heading next, and was disappointed to hear us say Niue.</i> <a href="https://www.bbc.com/travel/article/20160412-where-marrying-a-local-is-forbidden">[43_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>запитати</b> - звертатися до когось з питанням про кого-, що-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Дівчинка-підліток <b>запитала</b> про наступний пункт нашої подорожі і була розчарована, коли ми відповіли, що прямуємо на острів Ніуе.</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/04/160422_vert_tra_where_marrying_a_local_is_forbidden_vp">[43_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣6️⃣ associate / асоціюватися": 
    
    """
1️⃣6️⃣

💫 <b>associate / асоціюватися</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 106 / частота: 9</i>

🇬🇧 <b>associate</b> - to connect someone or something in your mind with someone or something else. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>In this way, it will always be <b>associated</b> with survival, with connotations and influences that run as deep as the blood in our veins.</i> <a href="https://www.bbc.com/future/article/20140827-how-the-colour-red-warps-the-mind">[90_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>асоціюватися</b> - поєднуватися в уявленні за асоціацією. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Таким чином, цей колір завжди буде <b>асоціюватися</b> з виживанням. І це сприйняття знаходиться так глибоко у підсвідомості, як і кров у наших жилах.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151023_vert_fut_how_the_colour_red_warps_the_mind_vp">[90_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣7️⃣ baby / малюк": 
    
    """
1️⃣7️⃣

💫 <b>baby / малюк</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 103 / частота: 30</i>

🇬🇧 <b>baby</b> - a very young child, especially one that has not yet begun to walk or talk. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>If you tickle a <b>baby</b> they apparently laugh because you are tickling them, not just because they are being tickled.</i> <a href="https://www.bbc.com/future/article/20150728-why-do-babies-laugh-out-loud">[56_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>малюк</b> - мала дитина. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Коли ви лоскочете свого <b>малюка</b> - він сміється, ймовірно, тому, що це саме ви його лоскочете.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150730_vert_fut_why_do_babies_laugh_vp">[56_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣8️⃣ bad / поганий": 
    
    """
1️⃣8️⃣

💫 <b>bad / поганий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 196 / частота: 107</i>

🇬🇧 <b>bad</b> - unpleasant and causing difficulties. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>So our attraction to <b>bad</b> news may be more complex than just journalistic cynicism or a hunger springing from the darkness within.</i> <a href="https://www.bbc.com/future/article/20140728-why-is-all-the-news-bad">[81_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>поганий</b> - який не має добрих якостей, властивостей; не такий, як треба; який викликає негативну оцінку. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Наша схильність до <b>поганих</b> новин насправді має більш складне пояснення, ніж звичайний цинізм журналістів або підсвідоме бажання побачити страхіття.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151217_vert_fut_why_is_all_the_news_bad_vp">[81_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣9️⃣ be / бути": 
    
    """
1️⃣9️⃣

💫 <b>be / бути</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 12192 / частота: 2199</i>

🇬🇧 <b>be</b> - used to say something about a person, thing, or state, to show a permanent or temporary quality, state, job, etc. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Now bots <b>are</b> more sophisticated,” he says. “They are better at disguising their identity and looking more like humans“.</i> <a href="https://www.bbc.com/future/article/20140609-how-online-bots-are-tricking-you">[53_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>бути</b> - уживається на означення наявності кого-, чого-небудь десь, у когось. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Зараз боти <b>є</b> більш досконалими," – пояснює дослідник. "Вони краще маскуються і більш схожі на людей".</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150818_vert_fut_how_online_bots_are_tricking_you_vp">[53_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣0️⃣ become / ставати": 
    
    """
2️⃣0️⃣

💫 <b>become / ставати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 288 / частота: 61</i>

🇬🇧 <b>become</b> - to start to be. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>But in Portugal, it <b>became</b> a part of the building. The decorative tiles are a construction material as well as decoration.</i> <a href="https://www.bbc.com/travel/article/20140515-the-story-behind-lisbons-beauty">[48_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>ставати</b> - виникати, зароджуватися, створюватися. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Але тільки в Португалії вона <b>стала</b> частиною будівлі. Декоративні кахлі виконують функцію і будівельного матеріалу, і орнаменту.</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/06/160601_vert_tra_the_story_behind_lisbons_beauty_vp">[48_BBC_Travel_Corpus_UKR]</a>
    """,

    "2️⃣1️⃣ begin / починатися": 
    
    """
2️⃣1️⃣

💫 <b>begin / починатися</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 205 / частота: 213</i>

🇬🇧 <b>begin</b> - to start to happen or exist. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Olson has spent a lifetime exploring the subtle ways of tricking people’s perception, and it all <b>began</b> with magic.</i> <a href="https://www.bbc.com/future/article/20150324-the-hidden-tricks-of-persuasion">[57_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>починатися</b> - починати здійснюватися, відбуватися, виявлятися. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Джей Олсон присвятив життя дослідженню засобів впливу на увагу людей. А <b>почалося</b> все з магії.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150717_vert_fut_the_hidden_tricks_of_persuasion_vp">[57_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣2️⃣ behaviour / поведінка": 
    
    """
2️⃣2️⃣

💫 <b>behaviour / поведінка</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 123 / частота: 144</i>

🇬🇧 <b>behaviour</b> - the way that someone behaves. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>To this day designers continue to shape the <b>behaviour</b> and the character of urban centres with subtle modifications to the built environment.</i> <a href="https://www.bbc.com/future/article/20131202-dirty-tricks-of-city-design">[55_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>поведінка</b> - сукупність чиїх-небудь дій і вчинків; спосіб життя. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Дизайнери і донині продовжують впливати на <b>поведінку</b> і характер міських мешканців шляхом непомітних архітектурних змін.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150707_vert_city_manipulates_behavior_vp">[55_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣3️⃣ believe / вірити": 
    
    """
2️⃣3️⃣

💫 <b>believe / вірити</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 192 / частота: 53</i>

🇬🇧 <b>believe</b> - to think that something is true, correct, or real. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Combine these unnerving findings with optimism bias – the tendency to <b>believe</b> you’re less at risk of things going wrong than other people – and you’re asking for trouble.</i> <a href="https://www.bbc.com/future/article/20160809-why-it-pays-to-be-grumpy-and-bad-tempered">[146_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>вірити</b> - бути впевненим, переконаним у чому-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Додайте до цього схильність людей <b>вірити</b> в те, що погане трапляється тільки з іншими, – і у нас є серйозний привід задуматися.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/09/160929_vert_fut_its_good_to_be_grumpy_and_bad_tempered_vp">[146_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣4️⃣ benefit / перевага": 
    
    """
2️⃣4️⃣

💫 <b>benefit / перевага</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 113 / частота: 134</i>

🇬🇧 <b>benefit</b> - a helpful or good effect, or something intended to help. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>According to psychologist Judith Kroll, learning a foreign language comes with a number of <b>benefits</b>, ranging from improved memory and mental flexibility to better cognitive creativity, and improved prioritisation skills.</i> <a href="https://www.bbc.com/future/article/20171108-the-translator-that-sits-in-your-ear">[131_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>перевага</b> - якість, властивість, що вигідно відрізняє кого-, що-небудь від когось, чогось. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>За словами психолога Джудіт Кролл, вивчаючи мови, людина отримує багато <b>переваг</b>: у неї покращуються не лише пам'ять і розумова гнучкість, а й когнітивна діяльність, здатність до творчості й уміння розставляти пріоритети.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-42493979">[131_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣5️⃣ big / великий": 
    
    """
2️⃣5️⃣

💫 <b>big / великий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 156 / частота: 306</i>

🇬🇧 <b>big</b> - large in size or amount. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Both would be amazing places to visit. They’re much <b>bigger</b> than anything on earth and that’s partly because Mars has a much thicker crust.</i> <a href="https://www.bbc.com/future/article/20161104-a-sightseers-guide-to-mars">[125_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>великий</b> - значний своїми розмірами, величиною. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Ці два місця (Гора Олімп і Долини Маринер) – найдивовижніші на всій планеті. Вони набагато <b>більші</b> за будь-яку природну споруду на Землі. Це частково пояснюється тим, що Марс має значно товстішу кору, ніж наша планета.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/11/161110_vert_fut_sightseers_guide_to_mars_vp">[125_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣6️⃣ blood / кров": 
    
    """
2️⃣6️⃣

💫 <b>blood / кров</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 167 / частота: 130</i>

🇬🇧 <b>blood</b> - the red liquid that is sent around the body by the heart, and carries oxygen and important substances to organs and tissue, and removes waste products. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Your heart is an incredibly hardworking organ. In five minutes, it will pump five litres of <b>blood</b> around your body.</i> <a href="https://www.bbc.com/future/article/20160520-the-incredible-things-we-know-about-your-heart-and-blood">[162_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>кров</b> - червона рідина, яка, циркулюючи в замкнутій кровоносній системі організму, забезпечує живлення його клітин і обмін речовин у ньому. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Наше серце – це неймовірно працьовитий орган. Упродовж п'яти хвилин воно прокачує п'ять літрів <b>крові</b>.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/05/160524_vert_fut_things_we_know_about_your_heart_and_blood_vp">[162_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣7️⃣ body / тіло": 
    
    """
2️⃣7️⃣

💫 <b>body / тіло</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 299 / частота: 59</i>

🇬🇧 <b>body</b> - the whole physical structure that forms a person or animal. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>But there’s a chemical component at work which is crucial for making sure those dream images are retained: noradrenaline. Noradrenaline is a hormone that primes the <b>body</b> and mind for action, and our levels of it are naturally lower in deep sleep.</i> <a href="https://www.bbc.com/future/article/20190516-why-cant-some-people-remember-their-dreams">[134_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>тіло</b> - організм людини або тварини в цілому з його зовнішніми і внутрішніми проявами. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Зберегти сни в пам'яті також допомагає хімічна речовина - норадреналін. Це гормон, який спонукає <b>тіло</b> і розум до активності, у глибокому сні його рівень знижується.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-48307939">[134_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣8️⃣ book / книга": 
    
    """
2️⃣8️⃣

💫 <b>book / книга</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 146 / частота: 64</i>

🇬🇧 <b>book</b> - a written text that can be published in printed or electronic form. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“I discovered the tremendous anger I had felt, without much awareness of it,” he explains. “It’s the most important thing I’ve done in my life.” He has just finished writing a <b>book</b> about the process.</i> <a href="https://www.bbc.com/future/article/20150818-what-is-it-like-to-have-never-felt-an-emotion">[64_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>книга</b> - зшиті в одну оправу аркуші паперу з якими-небудь записами. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Я виявив, що весь час відчував величезний гнів, не усвідомлюючи цього," - пояснює він. - "Це найголовніше, що я зробив у своєму житті". Він щойно завершив <b>книгу</b>, в якій описав цю нелегку подорож усередину своєї душі.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150826_vert_fut_live_without_emotions_vp">[64_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣9️⃣ brain / мозок": 
    
    """
2️⃣9️⃣

💫 <b>brain / мозок</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 382 / частота: 380</i>

🇬🇧 <b>brain</b> - the organ inside the head that controls thought, memory, feelings, and activity. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Our <b>brains</b> are kind of lazy,” he says. “We don’t look things up – we take bits and pieces of information from sources we trust, and jump to conclusions.”</i> <a href="https://www.bbc.com/future/article/20160225-chemonoia-the-fear-blinding-our-minds-to-real-dangers">[158_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>мозок</b> - центральний відділ нервової системи людини і тварини — речовина, що заповнює череп і канал хребта. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>“Наш <b>мозок</b> доволі ледачий,” – вважає дослідник. – “Ми не намагаємось аналізувати. Ми просто вихоплює фрагменти інформації з джерел, яким довіряємо, і робимо поспішні висновки.“</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/04/160413_vert_fut_chemonoia_the_fear_blinding_our_minds_to_real_dangers_vp">[158_BBC_Future_Corpus_UKR]</a>
    """,

    "3️⃣0️⃣ bring / приносити": 
    
    """
3️⃣0️⃣

💫 <b>bring / приносити</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 121 / частота: 37</i>

🇬🇧 <b>bring</b> - to take or carry someone or something to a place or a person, or in the direction of the person speaking. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>If you already believe that rain <b>brings</b> pain, you are more likely to notice the rainy days where you feel discomfort, and ignore those when you feel fine.</i> <a href="https://www.bbc.com/future/article/20150716-the-mysterious-ways-the-weather-changes-the-body-and-mind">[157_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>приносити</b> - несучи кого-, що-небудь, доставляти кудись. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Якщо ви заздалегідь впевнені, що дощ <b>приносить</b> вам погане самопочуття, ви, швидше за все, помітите саме ті дощові дні, коли ви відчували дискомфорт, і проігноруєте ті, коли все було прекрасно.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150721_vert_fut_weather_influence_health_vp">[157_BBC_Future_Corpus_UKR]</a>
    """,

    "3️⃣1️⃣ build / будувати": 
    
    """
3️⃣1️⃣

💫 <b>build / будувати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 172 / частота: 16</i>

🇬🇧 <b>build</b> - to make something by putting bricks or other materials together. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>What led Lake Titicaca’s Uros people to <b>build</b> entire islands for their villages?</i> <a href="https://www.bbc.com/travel/article/20140903-surreal-towns-shaped-by-nature">[35_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>будувати</b> - споруджувати, зводити яку-небудь будівлю (будівлі). <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Що змусило корінних мешканців узбережжя Тітікаки, індіанців уру, <b>будувати<b/> свої поселення на плавучих островах?</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/06/160603_vert_tra_surreal_towns_shaped_by_nature_vp">[35_BBC_Travel_Corpus_UKR]</a>
    """,

    "3️⃣2️⃣ can / могти": 
    
    """
3️⃣2️⃣

💫 <b>can / могти</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 2044 / частота: 1374</i>

🇬🇧 <b>can</b> - to be able to. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>The trend these days is towards wines to which nothing is added or removed. I <b>can</b> confidently say this isn't going to be on any serious wine list any time soon, but I wouldn't be surprised if it ended up in a bodega fridge near you soon.</i> <a href="https://www.bbc.com/travel/article/20161104-the-worlds-first-blue-wine">[17_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>могти</b> - бути в стані, в силах що-небудь робити. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Сьогодні в моді чисті вина без домішок. Я <b>можу</b> з упевненістю сказати, що синє вино не з'явиться найближчим часом у винній карті серйозного ресторану, але я не здивуюся, якщо його почнуть продавати у винному льосі по сусідству.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-38056958">[17_BBC_Travel_Corpus_UKR]</a>
    """,

    "3️⃣3️⃣ case / випадок": 
    
    """
3️⃣3️⃣

💫 <b>case / випадок</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 168 / частота: 153</i>

🇬🇧 <b>case</b> - a particular situation or example of something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Then there was the <b>case</b> of the 15 year old girl who in 2005 was found curled up asleep at the top of a 130ft crane, having climbed there while sleepwalking.</i> <a href="https://www.bbc.com/future/article/20120208-it-is-dangerous-to-wake-a-sleepwa">[156_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>випадок</b> - обставини, стан речей, ситуація. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Був ще <b>випадок</b> із 15-річною дівчиною, яку знайшли в кабіні вантажного крана на сорокаметровій висоті, - вона залізла туди уві сні, згорнулася клубочком і продовжувала спати.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-45446558">[156_BBC_Future_Corpus_UKR]</a>
    """,

    "3️⃣4️⃣ cell / клітина": 
    
    """
3️⃣4️⃣

💫 <b>cell / клітина</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 115 / частота: 86</i>

🇬🇧 <b>cell</b> - the smallest basic unit of a plant or animal. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>The antibodies primed immune system <b>cells</b> in the skin and gut to quickly repel any parasite trying to push its way in.</i> <a href="https://www.bbc.com/future/article/20150409-why-do-we-have-allergies">[138_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>клітина</b> - найпростіша одиниця будови організму, яка складається з протоплазми, ядра та оболонки. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Антитіла активують <b>клітини</b> імунної системи на шкірі і в кишечнику, щоб якомога швидше зупинити спробу паразита проникнути в організм.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/08/160817_vert_fut_why_do_we_have_allergies_vp">[138_BBC_Future_Corpus_UKR]</a>
    """,

    "3️⃣5️⃣ century / століття": 
    
    """
3️⃣5️⃣

💫 <b>century / століття</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 214 / частота: 167</i>

🇬🇧 <b>century</b> - a period of 100 years. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Built between the 7th and 8th <b>Century</b> BC, the underground complex was built to defend against attacks from marauding armies.</i> <a href="https://www.bbc.com/travel/article/20150821-six-lesser-known-wonders-of-the-ancient-world">[79_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>століття</b> - сас, період тривалістю сто років; сторіччя, вік. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Підземний комплекс звели між VII і VIII <b>століттями</b> до нашої ери для захисту місцевих жителів від набігів кочовиків-мародерів.</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/10/161003_vert_tra_six_lesser_known_wonders_of_the_ancient_world_vp">[79_BBC_Travel_Corpus_UKR]</a>
    """,

    "3️⃣6️⃣ certain / певний": 
    
    """
3️⃣6️⃣

💫 <b>certain / певний</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 108 / частота: 245</i>

🇬🇧 <b>certain</b> - having no doubt or knowing exactly that something is true, or known to be true, correct, exact, or effective. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>And you can be <b>certain</b> that somewhere in the world, somebody is pulling cash out of their pocket to buy something.</i> <a href="https://www.bbc.com/future/article/20150724-the-truth-about-the-death-of-cash">[98_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>певний</b> - який твердо вірить у що-небудь, не сумнівається у чомусь; упевнений. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>І будете <b>певні</b>, що кожної миті десь у світі хтось намацує у кишені готівку, щоби купити щось.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/09/160909_vert_fut_truth_about_the_death_of_cash_vp">[98_BBC_Future_Corpus_UKR]</a>
    """,

    "3️⃣7️⃣ chance / шанс": 
    
    """
3️⃣7️⃣

💫 <b>chance / шанс</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 102 / частота: 79</i>

🇬🇧 <b>chance</b> - an occasion that allows something to be done. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>If Scotland doesn’t sweep Poyais up, someone else will – and there goes the nation’s one <b>chance</b> at colonial greatness.</i> <a href="https://www.bbc.com/future/article/20160127-the-conman-who-pulled-off-historys-most-audacious-scam">[97_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>шанс</b> - умова, яка забезпечує удачу, успіх у чому-небудь; ймовірність, можливість здійснення чогось. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Якщо шотландці не захоплять Пояїс, це зробить хтось інший, і нація втратить свій єдиний <b>шанс</b> отримати колонії.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/01/160129_vert_most_audacious_scam_vp">[97_BBC_Future_Corpus_UKR]</a>
    """,

    "3️⃣8️⃣ change / змінювати": 
    
    """
3️⃣8️⃣

💫 <b>change / змінювати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 262 / частота: 47</i>

🇬🇧 <b>change</b> - to exchange one thing for another thing, especially of a similar type. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>At the very least, the research could <b>change</b> the way we view this often under-appreciated part of our lives.</i> <a href="https://www.bbc.com/future/article/20140721-how-to-learn-while-you-sleep">[28_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>змінювати</b> - робити іншим, інакшим; міняти. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Принаймні ці дослідження можуть <b>змінити</b> уявлення про ту частину нашого життя, якій ми зазвичай не надаємо належного значення.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/05/160530_vert_fut_how_to_learn_while_you_sleep_vp">[28_BBC_Future_Corpus_UKR]</a>
    """,

    "3️⃣9️⃣ child / дитина": 
    
    """
3️⃣9️⃣

💫 <b>child / дитина</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 291 / частота: 97</i>

🇬🇧 <b>child</b> - a boy or girl from the time of birth until he or she is an adult, or a son or daughter of any age. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Praising a <b>child’s</b> intelligence can teach them that this is a fixed trait that they can’t control.</i> <a href="https://www.bbc.com/future/article/20140204-is-it-right-to-praise-a-child">[184_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>дитина</b> - маленька дівчинка або маленький хлопчик. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Коли ви хвалите <b>дитину</b> за її інтелект, це вчить її, що ця риса є постійною і вона нічого не може зробити, щоби її покращити.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151008_vert_fut_is_it_right_to_praise_a_child_vp">[184_BBC_Future_Corpus_UKR]</a>
    """,

    "4️⃣0️⃣ choose / обирати": 
    
    """
4️⃣0️⃣

💫 <b>choose / обирати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 106 / частота: 56</i>

🇬🇧 <b>choose</b> - to decide what you want from two or more things or possibilities. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>There’s also the fact that, often, what mankind <b>chooses</b> to preserve is not always what is most revealing – or interesting about us.</i> <a href="https://www.bbc.com/future/article/20151127-how-will-future-archaeologists-study-us">[91_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>обирати</b> - надавати перевагу комусь, чомусь перед ким-, чим-небудь іншим. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Існує і ще один момент. Те, що людство <b>обирає</b> в якості найважливішою інформації про свою цивілізацію, згодом видається далеко не самим показовим або цікавим.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151201_vert_fut_how_will_future_archaeologists_study_us_vp">[91_BBC_Future_Corpus_UKR]</a>
    """,

    "4️⃣1️⃣ city / місто": 
    
    """
4️⃣1️⃣

💫 <b>city / місто</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 286 / частота: 345</i>

🇬🇧 <b>city</b> - a large town. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>My next stop was Aarhus, Denmark’s second biggest <b>city</b>, to visit the breathtaking new Moesgaard Museum that’s home to one of the best exhibits on Iron Age Europe.</i> <a href="https://www.bbc.com/travel/article/20161014-a-2000-year-old-unsolved-mystery">[08_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>місто</b> - великий населений пункт; адміністративний, промисловий, торговий і культурний центр. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Моя наступна зупинка - Орхус - друге за величиною <b>місто</b> в Данії, куди я приїхав подивитися дивовижні експонати, виставлені в новому Музеї Моесгорд. Тут зберігається одна з найкращих експозицій, присвячених залізному віку в Європі.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-38315852">[08_BBC_Travel_Corpus_UKR]</a>
    """,

    "4️⃣2️⃣ claim / стверджувати": 
    
    """
4️⃣2️⃣

💫 <b>claim / стверджувати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 103 / частота: 31</i>

🇬🇧 <b>claim</b> - to say that something is true or is a fact, although you cannot prove it and other people might not believe it. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Called ‘medical sanguinarians’, these people <b>claim</b> that a regular dose of human blood can alleviate various medical conditions; from headaches and fatigue to severe stomach pains that otherwise cannot effectively be treated.</i> <a href="https://www.bbc.com/future/article/20160520-the-incredible-things-we-know-about-your-heart-and-blood">[162_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>стверджувати</b> - доводити, підтверджувати достовірність, правильність чого-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Ці "медичні вампіри" <b>стверджують</b>, що регулярний прийом крові допомагає їм полегшити такі симптоми, як головний біль, втому, біль у шлунку, на які не діє жодне інше лікування.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/05/160524_vert_fut_things_we_know_about_your_heart_and_blood_vp">[162_BBC_Future_Corpus_UKR]</a>
    """,

    "4️⃣3️⃣ colour / колір": 
    
    """
4️⃣3️⃣

💫 <b>colour / колір</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 169 / частота: 216</i>

🇬🇧 <b>colour</b> - red, blue, green, yellow, etc. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>The human eye can physically perceive millions of <b>colours</b>. But we don’t all recognise these colours in the same way.</i> <a href="https://www.bbc.com/future/article/20180419-the-words-that-change-the-colours-we-see">[12_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>колір</b> - світловий тон чого-небудь; забарвлення. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Людське око здатне сприймати мільйони <b>кольорів</b>. Але визначаємо ми їх далеко не однаково.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-44008630">[12_BBC_Future_Corpus_UKR]</a>
    """,

    "4️⃣4️⃣ come / прийти": 
    
    """
4️⃣4️⃣

💫 <b>come / прийти</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 388 / частота: 45</i>

🇬🇧 <b>come</b> - to move or travel towards the speaker or with the speaker. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Azulejos first <b>came</b> to Portugal in the 15th Century, when parts of the Iberian Peninsula were still under Moorish rule.</i> <a href="https://www.bbc.com/travel/article/20140515-the-story-behind-lisbons-beauty">[48_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>прийти</b> - йдучи, з'являтися десь, у когось; прибувати куди-небудь, до когось пішки. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Мистецтво азулежу <b>прийшло</b> в Португалію в XV столітті, коли переважна частина Піренейського півострова перебувала під мавританським правлінням.</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/06/160601_vert_tra_the_story_behind_lisbons_beauty_vp">[48_BBC_Travel_Corpus_UKR]</a>
    """,

    "4️⃣5️⃣ common / звичайний": 
    
    """
4️⃣5️⃣

💫 <b>common / звичайний</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 112 / частота: 99</i>

🇬🇧 <b>common</b> - the same in a lot of places or for a lot of people. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Every year, the <b>common</b> black hawk returns from its winter migration to Arizona’s Verde Valley in late March. “It’s amazing. It’s like a wonderful harbinger of spring,” Green said.</i> <a href="https://www.bbc.com/travel/article/20170719-the-mysterious-origins-of-europes-oldest-language">[28_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>звичайний</b> - який нічим не виділяється серед інших, не має яких-небудь специфічних, визначних особливостей; простий. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Щороку наприкінці березня в аризонську долину Верде повертається з зимівлі <b>звичайний</b> чорний канюк. "Він прекрасний. Канюк - дивовижний провісник весни", - сказала Грін.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-40729382">[26_BBC_Travel_Corpus_UKR]</a>
    """,

    "4️⃣6️⃣ compare / порівнювати": 
    
    """
4️⃣6️⃣

💫 <b>compare / порівнювати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 122 / частота: 39</i>

🇬🇧 <b>compare</b> - to examine or look for the difference between two or more things. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Language evolution can be <b>compared</b> to biological evolution, but whereas genetic change is driven by environmental pressures, languages change and develop through social pressures.</i> <a href="https://www.bbc.com/future/article/20160811-the-amazing-benefits-of-being-bilingual">[27_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>порівнювати</b> - вимірюючи, розглядаючи, досліджуючи і т. ін. які-небудь однорідні предмети, явища тощо, виявляти в них однакові риси або відмінності, переваги або недоліки і т. ін. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Еволюцію мови можна <b>порівняти</b> з біологічною еволюцією, але якщо генетичні зміни відбуваються через вплив навколишнього середовища, мови розвиваються завдяки соціальним чинникам.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/08/160816_vert_fut_amazing_benefits_of_being_bilingual_vp">[27_BBC_Future_Corpus_UKR]</a>
    """,

    "4️⃣7️⃣ consider / розглядати": 
    
    """
4️⃣7️⃣

💫 <b>consider / розглядати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 162 / частота: 12</i>

🇬🇧 <b>consider</b> - to spend time thinking about a possibility or making a decision. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>First <b>consider</b> the senses that relate to the position of our bodies. Close your eyes, and then touch your right forefinger to your left elbow tip. Easy?</i> <a href="https://www.bbc.com/future/article/20141118-how-many-senses-do-you-have">[61_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>розглядати</b> - вивчати, оцінювати кого-небудь, досліджувати, аналізувати щось. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Давайте спершу <b>розглянемо</b> чуття, яке відповідає за сприйняття нашого тіла в просторі. Заплющте очі, а потім торкніться лівого ліктя вказівним пальцем правої руки. Це не важко, так?</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150917_vert_fut_how_many_senses_do_you_have_vp">[61_BBC_Future_Corpus_UKR]</a>
    """,

    "4️⃣8️⃣ control / контролювати": 
    
    """
4️⃣8️⃣

💫 <b>control / контролювати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 155 / частота: 22</i>

🇬🇧 <b>control</b> - to order, limit, or rule something, or someone's actions or behaviour. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>The right side of the brain <b>controls</b> the left hand, and vice versa. And so being left-handed can have knock-on effects on the way the brain is arranged.</i> <a href="https://www.bbc.com/future/article/20160930-the-mystery-of-why-left-handers-are-so-much-rarer">[24_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>контролювати</b> - перевіряти кого-, що-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Ліву руку <b>контролює</b> права півкуля мозку, і навпаки, тому у шульг мозок може бути влаштований трохи інакше.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-39667412">[24_BBC_Future_Corpus_UKR]</a>
    """,

    "4️⃣9️⃣ country / країна": 
    
    """
4️⃣9️⃣

💫 <b>country / країна</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 265 / частота: 305</i>

🇬🇧 <b>country</b> - an area of land that has its own government, army, etc. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>What happens to the bag depends on the <b>country</b>. In some countries, the luggage gets destroyed. In the UK, the airlines tend to send them to auction.</i> <a href="https://www.bbc.com/future/article/20150907-did-an-airline-auction-off-your-luggage">[76_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>країна</b> - територія, що становить єдність із погляду історії, природних умов, населення тощо. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Що відбувається із сумкою далі залежить від <b>країни</b>. У деяких країнах багаж просто знищують, у Великій Британії авіакомпанії зазвичай відправляють його на аукціон.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150909_vert_fut_did_an_airline_auction_off_your_luggage_vp">[76_BBC_Future_Corpus_UKR]</a>
    """,

    "5️⃣0️⃣ course / курс": 
    
    """
5️⃣0️⃣

💫 <b>course / курс</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 148 / частота: 16</i>

🇬🇧 <b>course</b> - a set of classes or a plan of study on a particular subject, usually leading to an exam or qualification. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>The app says that some 1.1 million users have signed up to do one of the Esperanto <b>courses</b> – half of the people who actually speak it.</i> <a href="https://www.bbc.com/future/article/20180110-the-invented-language-that-found-a-second-life-online">[132_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>курс</b> - закінчений цикл навчання, його обсяг і час, за який цей цикл навчання відбувається. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Як свідчить програма, на <b>курс есперанто</b> підписалися близько 1,1 млн користувачів - майже половина всіх людей, які говорять есперанто в світі.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-42654538">[132_BBC_Future_Corpus_UKR]</a>
    """,

    "5️⃣1️⃣ create / створювати": 
    
    """
5️⃣1️⃣

💫 <b>create / створювати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 158 / частота: 85</i>

🇬🇧 <b>create</b> - to make something new, or invent something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>But we are not tapping into a new area of the brain. We <b>create</b> new connections between nerve cells or lose old connections that we no longer need.</i> <a href="https://www.bbc.com/future/article/20121112-do-we-only-use-10-of-our-brains">[173_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>створювати</b> - винаходити, виробляти, виводити що-небудь нове, раніше невідоме. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Але це не означає, що нам вдається задіяти зовсім іншу ділянку мозку. Ми лише <b>створюємо</b> нові зв'язки між нейронами або втрачаємо старі, які нам більше не потрібні.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-41751478">[173_BBC_Future_Corpus_UKR]</a>
    """,

    "5️⃣2️⃣ culture / культура": 
    
    """
5️⃣2️⃣

💫 <b>culture / культура</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 158 / частота: 137</i>

🇬🇧 <b>culture</b> - the way of life, especially the general customs and beliefs, of a particular group of people at a particular time. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Our <b>culture</b> may also determine the way we talk about our memories, with some psychologists arguing that they only come once we have mastered the power of speech.</i> <a href="https://www.bbc.com/future/article/20160726-the-mystery-of-why-you-cant-remember-being-a-baby">[165_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>культура</b> - сукупність матеріальних і духовних цінностей, створених людством протягом його історії. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Наша <b>культура</b> також визначає, як ми розповідаємо про спогади. На думку деяких психологів, здатність формувати яскраві автобіографічні спогади приходить тільки з розвитком мовлення.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/07/160727_vert_fut_mystery_of_why_you_cant_remember_being_a_baby_vp">[165_BBC_Future_Corpus_UKR]</a>
    """,

    "5️⃣3️⃣ day / день": 
    
    """
5️⃣3️⃣

💫 <b>day / день</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 510 / частота: 182</i>

🇬🇧 <b>day</b> - a period of 24 hours, especially from twelve o'clock one night to twelve o'clock the next night. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>After spending a <b>day</b> in Getaria, I drove 26km east along the Bay of Biscay coast to San Sebastian, a Basque city renowned for its restaurants and beaches.</i> <a href="https://www.bbc.com/travel/article/20170719-the-mysterious-origins-of-europes-oldest-language">[28_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>день</b> - частина доби від сходу до заходу сонця, від ранку до вечора. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Провівши <b>день</b> у Гетарії, я поїхала на схід уздовж Біскайського узбережжя до баскського міста Сан-Себастьян, що славиться своїми ресторанами та пляжами.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-40729382">[28_BBC_Travel_Corpus_UKR]</a>
    """,

    "5️⃣4️⃣ describe / описувати": 
    
    """
5️⃣4️⃣

💫 <b>describe / описувати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 109 / частота: 55</i>

🇬🇧 <b>describe</b> - to say or write what someone or something is like. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“The company present… say that the flash was very great and the crack as loud as a pistol,” he later wrote. “I then felt what I know not how well to <b>describe</b>.“</i> <a href="https://www.bbc.com/future/article/20150422-how-not-to-be-stupid">[35_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>описувати</b> - в усній або письмовій формі розповідати про кого-, що-небудь; змальовувати когось, щось мовними засобами. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Присутні при експерименті ще довго згадували неймовірний спалах і гучний звук, як від пострілу пістолета, – писав науковець пізніше. – А я навіть не можу <b>описати</b>, що я відчув."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151020_vert_fut_how_not_to_be_stupid_vp">[35_BBC_Future_Corpus_UKR]</a>
    """,

    "5️⃣5️⃣ design / дизайн": 
    
    """
5️⃣5️⃣

💫 <b>design / дизайн</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 65 / частота: 26</i>

🇬🇧 <b>design</b> - a drawing or set of drawings showing how a building or product is to be made and how it will work and look. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Successful <b>design</b> is not so much about how our buildings can shape us, as Churchill had it, but about making people feel they have some control over their environment."</i> <a href="https://www.bbc.com/future/article/20170605-the-psychology-behind-your-citys-design">[15_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>дизайн</b> - художньо-конструкторська діяльність, спрямована на створення нових видів і типів виробів, які б відповідали вимогам суспільства. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Вдалий <b>дизайн</b> не означає, що будівлі можуть змінювати наше сприйняття, як вважав Черчілль, він радше повинен давати мешканцям міста відчуття, що вони певною мірою можуть керувати своїм навколишнім середовищем."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-40186983">[15_BBC_Future_Corpus_UKR]</a>
    """,

    "5️⃣6️⃣ develop / розвиватися": 
    
    """
5️⃣6️⃣

💫 <b>develop / розвиватися</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 125 / частота: 47</i>

🇬🇧 <b>develop</b> - to (cause something to) grow or change into a more advanced, larger, or stronger form. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Since it occurs at such an early age of development, the cells can become incorporated into the tissue and seem to <b>develop</b> normally, yet they are carrying another person’s genetic blueprint."</i> <a href="https://www.bbc.com/future/article/20150917-is-another-human-living-inside-you">[87_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>розвиватися</b> - ставати кращим, досконалішим, підніматися на вищий щабель, досягати високого рівня у чому-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Оскільки це відбувається на дуже ранньому етапі, 'чужі' клітини потрапляють у тканини організму і нормально <b>розвиваються</b>, але при цьому несуть генетичну програму іншої людини."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150922_vert_fut_another_human_living_inside_you_vp">[87_BBC_Future_Corpus_UKR]</a>
    """,

    "5️⃣7️⃣ difference / відмінність": 
    
    """
5️⃣7️⃣

💫 <b>difference / відмінність</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 184 / частота: 53</i>

🇬🇧 <b>difference</b> - the way in which two or more things which you are comparing are not the same. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"But while <b>differences</b> in personality do exist between cultures and nations, they often don’t match up with the widely held stereotypes of national character."</i> <a href="https://www.bbc.com/future/article/20170413-different-nationalities-really-have-different-personalities">[20_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>відмінність</b> - яке чимось відрізняється від кого-, чого-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Проте, хоча нації й відрізняються рисами характеру, ці <b>відмінності</b> абсолютно не збігаються із загальними стереотипами."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-39641118">[20_BBC_Future_Corpus_UKR]</a>
    """,

    "5️⃣8️⃣ different / інший": 
    
    """
5️⃣8️⃣

💫 <b>different / інший</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 363 / частота: 1247</i>

🇬🇧 <b>different</b> - not the same. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"While Molaison couldn’t remember details of personal events, for instance, he could learn new “procedural” skills since they are processed in <b>different</b> parts of the brain."</i> <a href="https://www.bbc.com/future/article/20150630-my-dentist-saved-my-tooth-but-stole-my-memory">[45_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>інший</b> - який відрізняється від названого, даного; який існує, перебуває не в цьому місці, не в цих обставинах; не цей, не той, другий. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Генрі Молісон, наприклад, не міг згадати подробиці особистих події, але навчався нових "процедурних" навичок, оскільки вони обробляються в <b>інших</b> відділах мозку."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150820_vert_fut_dentist_extracted_memory_vp">[45_BBC_Future_Corpus_UKR]</a>
    """,

    "5️⃣9️⃣ discover / відкривати": 
    
    """
5️⃣9️⃣

💫 <b>discover / відкривати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 113 / частота: 108</i>

🇬🇧 <b>discover</b> - to find information, a place, or an object, especially for the first time. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"In looking into agnotology, I <b>discovered</b> the secret world of classified science, and thought historians should be giving this more attention."</i> <a href="https://www.bbc.com/future/article/20160105-the-man-who-studies-the-spread-of-ignorance">[115_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>відкривати</b> - піднімаючи або знімаючи те, чим закрите, накрите щось, робити вільним доступ усередину чого-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Досліджуючи агнотологію, я <b>відкрив</b> цілий таємний світ секретної науки, і подумав, що історики мають приділити цьому явищу більше уваги."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/02/160209_vert_fut_the_man_who_studies_the_spread_of_ignorance_vp">[115_BBC_Future_Corpus_UKR]</a>
    """,

    "6️⃣0️⃣ do / робити": 
    
    """
6️⃣0️⃣

💫 <b>do / робити</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 1174 / частота: 249</i>

🇬🇧 <b>do</b> - to perform, take part in, or achieve something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Whichever way you choose to wash and dry your hands, the main finding from research is to <b>do</b> it for longer than you think."</i> <a href="https://www.bbc.com/future/article/20170519-does-it-matter-how-you-wash-and-dry-your-hands">[18_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>робити</b> - займатися якою-небудь справою, діяльністю. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Неважливо, як саме ви миєте руки, головне <b>робити</b> це довше, ніж ви вважаєте за потрібне."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-40015296">[18_BBC_Future_Corpus_UKR]</a>
    """,

    "6️⃣1️⃣ drink / пити":

    """
6️⃣1️⃣

💫 <b>drink / пити</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 200 / частота: 26</i>

🇬🇧 <b>drink</b> - to take liquid into the body through the mouth. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"When I was a kid no-one <b>drank</b> tea. If someone <b>drank</b> tea, they’d joke and say he was an addict,” recalled Ahmad Rahnama, referring the stereotype that opium addicts <b>drink</b> a lot of tea."</i> <a href="https://www.bbc.com/travel/article/20180109-irans-ancient-village-of-little-people">[23_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>пити</b> - ковтати яку-небудь рідину для вгамування спраги. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"У моєму дитинстві в нас не було заведено <b>пити</b> чай. Якщо хтось <b>пив</b> чай, його називали наркоманом", - згадує Ахмад Рахнама, натякаючи на повір'я, що курці опіуму зазвичай <b>пили</b> багато чаю."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-42705451">[23_BBC_Travel_Corpus_UKR]</a>
    """,

    "6️⃣2️⃣ easy / простий":

    """
6️⃣2️⃣

💫 <b>easy / простий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 160 / частота: 73</i>

🇬🇧 <b>easy</b> - needing little effort. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"But an azulejos revival started in the 1950s, when Lisbon’s first metro station designers wanted a low-maintenance, <b>easy</b> way to have the underground spaces feel less separate from the outside world."</i> <a href="https://www.bbc.com/travel/article/20140515-the-story-behind-lisbons-beauty">[48_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>простий</b> - неважкий, легкий для розуміння, здійснення, виконання. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Відродження художнього стилю почалося в 1950-і роки, коли інженери і дизайнери перших станцій лісабонського метро вирішили в <b>простий</b> спосіб відтворити зовнішній вигляд португальської столиці під землею."</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/06/160601_vert_tra_the_story_behind_lisbons_beauty_vp">[48_BBC_Travel_Corpus_UKR]</a>
    """,

    "6️⃣3️⃣ eat / їсти":

    """
6️⃣3️⃣

💫 <b>eat / їсти</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 191 / частота: 49</i>

🇬🇧 <b>eat</b> - to put or take food into the mouth, chew it (= crush it with the teeth), and swallow it. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"They continued to <b>eat</b> at the same time, but because the clocks had changed, their 1pm lunches became 2pm lunches, and they were suddenly eating their 8pm dinners at 9pm."</i> <a href="https://www.bbc.com/travel/article/20170504-the-strange-reason-spaniards-eat-late">[20_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>їсти</b> - споживати їжу. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Вони просто продовжили, як і раніше, <b>їсти</b> в звичний для себе час, і отже, обід пересунувся на другу годину, а вечеря - на дев'яту."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-39849128">[20_BBC_Travel_Corpus_UKR]</a>
    """,

    "6️⃣4️⃣ effect / ефект":

    """
6️⃣4️⃣

💫 <b>effect / ефект</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 233 / частота: 143</i>

🇬🇧 <b>effect</b> - the result of a particular influence. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Clearly, studying the effect of colour is much harder than it looks - or maybe colours just don’t have the <b>effect</b> that we expect."</i> <a href="https://www.bbc.com/future/article/20150402-do-colours-really-change-our-mood">[107_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>ефект</b> - сильне враження, викликане ким-, чим-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Насправді вивчати вплив кольорів на психіку – набагато важче, ніж здається на перший погляд. Можливо просто кольори дають зовсім не той <b>ефект</b>, якого ми очікуємо."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/06/160621_vert_fut_do_colours_really_change_our_mood_vp">[107_BBC_Future_Corpus_UKR]</a>
    """,

    "6️⃣5️⃣ emotion / емоція":

    """
6️⃣5️⃣

💫 <b>emotion / емоція</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 103 / частота: 126</i>

🇬🇧 <b>emotion</b> - a strong feeling such as love or anger, or strong feelings in general. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Decisions based on negative <b>emotions</b> can also work the other way. A growing body of evidence shows that voters unconsciously punish politicians when things don’t go their way – even issues entirely unconnected to politics."</i> <a href="https://www.bbc.com/future/article/20150506-the-dark-psychology-of-voting">[52_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>емоція</b> - переживання людиною свого ставлення до дійсності, до особистого й навколишнього життя; душевне переживання, почуття людини. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Негативні <b>емоції</b> можуть працювати і в іншому напрямку. Чимало досліджень доводять, що люди схильні несвідомо карати кандидатів за речі, які насправді не дуже пов'язані з політикою."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150908_vert_fut_hidden_psychology_of_voting_vp">[52_BBC_Future_Corpus_UKR]</a>
    """,

    "6️⃣6️⃣ end / кінець":

    """
6️⃣6️⃣

💫 <b>end / кінець</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 147 / частота: 67</i>

🇬🇧 <b>end</b> - the part of a place or thing that is furthest away from the centre. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"As Amsterdam is mostly built on water, the houses are not completely straight,' warned Hinterstoisser. 'If you put a tennis ball on one <b>end</b> of my living room, it will roll all by itself quite swiftly to the other side.'"</i> <a href="https://www.bbc.com/travel/article/20150529-living-in-the-worlds-safest-cities">[68_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>кінець</b> - крайній пункт, межа протяглості предмета, площини тощо, а також те, що прилягає до такого пункту, межі. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"'Оскільки Амстердам побудований переважно на воді, будинки тут не зовсім рівні,' попереджає Хінтертойссер. 'Якщо покласти тенісний м'ячик на підлогу в одному кутку моєї вітальні, він швидко перекотиться в протилежний <b>кінець</b> кімнати'."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-40521665">[68_BBC_Travel_Corpus_UKR]</a>
    """,

    "6️⃣7️⃣ even / навіть":

    """
6️⃣7️⃣

💫 <b>even / навіть</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 746 / частота: 529</i>

🇬🇧 <b>even</b> - used to show that something is surprising, unusual, unexpected, or extreme. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"<b>Even</b> if you are too busy or tired to do serious study, just practising a dialogue or listening to a foreign pop song can help, says Simcott."</i> <a href="https://www.bbc.com/future/article/20150528-how-to-learn-30-languages">[41_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>навіть</b> - вживається для виділення і підсилення значення того слова або словосполучення, якого стосується. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"<b>Навіть</b> якщо ви дуже зайняті або втомлені для серйозного навчання, просто повторюйте діалог або прослухайте пісню іноземною мовою, каже Річард Сімкотт."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150804_vert_fut_how_to_learn_30_languages_vp">[41_BBC_Future_Corpus_UKR]</a>
    """,

    "6️⃣8️⃣ event / подія":

    """
6️⃣8️⃣

💫 <b>event / подія</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 123 / частота: 125</i>

🇬🇧 <b>event</b> - anything that happens, especially something important or unusual. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"That <b>event</b> became known as the Revolution of Dwarves," Förster said. “It showed the world that communism was unravelling, and that people of all ages could join together to fight against the system peacefully.”</i> <a href="https://www.bbc.com/travel/article/20171017-the-truth-behind-wrocaws-cheeky-gnomes">[54_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>подія</b> - те, що відбувалося або відбулося, сталося; явище, факт суспільного або особистого життя. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Ця <b>подія</b> отримала назву "Революція гномів," - розповідає Ферстер. - Вона показала світу, що комуністичному режиму приходить кінець, і що люди різного віку можуть об'єднатися, щоби мирно боротися проти системи".</i> <a href="https://www.bbc.com/ukrainian/vert-tra-41696253">[54_BBC_Travel_Corpus_UKR]</a>
    """,

    "6️⃣9️⃣ ever / коли-небудь":

    """
6️⃣9️⃣

💫 <b>ever / коли-небудь</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 120 / частота: 13</i>

🇬🇧 <b>ever</b> - at any time. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Andrey Begunov, the Chief Information Officer of PUMB, a large financial institution owned by Ukrainian billionaire Rinat Akhmetov, says that in his 23 years within the banking and IT sectors of Ukraine, this was the worst situation he’s <b>ever</b> seen."</i> <a href="https://www.bbc.com/future/article/20170704-the-day-a-mysterious-cyber-attack-crippled-ukraine">[202_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>коли-небудь</b> - у будь-який час. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Директор департаменту інформаційних технологій банку ПУМБ Андрій Бегунов заявив, що за 23 роки роботи в банківській та ІТ-галузі України це була найгірша ситуація, яку він <b>коли-небудь</b> бачив."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-40511484">[202_BBC_Future_Corpus_UKR]</a>
    """,

    "7️⃣0️⃣ everyone / кожний": 
    
    """
7️⃣0️⃣

💫 <b>everyone / кожний</b> 💫

🔹 <i>pronoun / займенник</i>
🔹 <i>frequency: 105 / частота: 245</i>

🇬🇧 <b>everyone</b> - every person. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"<b>Everyone</b> has experienced that feeling of utter bewilderment when the alarm awakens you from deep sleep, instead of the lighter sleep we are usually experiencing by the time our alarms sound."</i> <a href="https://www.bbc.com/future/article/20120208-it-is-dangerous-to-wake-a-sleepwa">[156_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>кожний</b> - один з усіх, узятий окремо; будь-який з даного ряду; всякий. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"<b>Кожному</b> з нас знайоме це відчуття повної розгубленості, коли дзвінок будильника вривається у вашу свідомість на фазі глибокого сну, а не поверхневого, в якому ми зазвичай перебуваємо у той момент, коли нам потрібно прокидатися."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-45446558">[156_BBC_Future_Corpus_UKR]</a>
    """,

    "7️⃣1️⃣ everything / все": 
    
    """
7️⃣1️⃣

💫 <b>everything / все</b> 💫

🔹 <i>pronoun / займенник</i>
🔹 <i>frequency: 101 / частота: 818</i>

🇬🇧 <b>everything</b> - all things. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"The bog flowed slowly and hungrily, preserving <b>everything</b> that fell into it for millennia, a reminder of its everlasting and awesome power."</i> <a href="https://www.bbc.com/travel/article/20161014-a-2000-year-old-unsolved-mystery">[08_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>все</b> - означає щось як ціле, неподільне, взяте повністю. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Поверхня болота повільно і жадібно колихалась, ніби нагадуючи про свою потужну і містичну силу тисячоліттями зберігати <b>все</b>, що потрапить в трясовину."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-38315852">[08_BBC_Travel_Corpus_UKR]</a>
    """,

   "7️⃣2️⃣ evidence / доказ": 
    
    """
7️⃣2️⃣

💫 <b>evidence / доказ</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 176 / частота: 57</i>

🇬🇧 <b>evidence</b> - facts, information, documents, etc. that give reason to believe that something is true. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"So there isn’t good <b>evidence</b> that dairy products lead to the production of more mucus. But it does seem to leave some people feeling more uncomfortable, which would explain why some claim there’s a link and others don’t."</i> <a href="https://www.bbc.com/future/article/20170421-should-you-avoid-ice-cream-when-you-have-a-cold">[17_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>доказ</b> - незаперечний довід або факт, який підтверджує істинність чого-небудь; підтвердження. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Отже, <b>доказів</b> того, що молочні продукти підвищують секрецію слизу, насправді немає. Але в деяких людей дійсно виникає відчуття дискомфорту в горлі після випитого молока. Хоча причина - зовсім в іншому."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-39707115">[17_BBC_Future_Corpus_UKR]</a>
    """,

    "7️⃣3️⃣ example / приклад": 
    
    """
7️⃣3️⃣

💫 <b>example / приклад</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 257 / частота: 69</i>

🇬🇧 <b>example</b> - something that is typical of the group of things that it is a member of. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"The peaceful interweaving of the two nations has attracted the interest of advisors to Israeli prime minister Benjamin Netanyahu, as an <b>example</b> of how two different communities can live harmoniously together."</i> <a href="https://www.bbc.com/travel/article/20171210-europes-strange-border-anomaly">[67_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>приклад</b> - те, що варто наслідувати; зразок. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Мирне співіснування двох націй навіть привернуло увагу радників прем'єр-міністра Ізраїлю Біньяміна Нетаньягу. Вони вивчають <b>приклад</b> того, як дві різні громади можуть жити разом у гармонії."</i> <a href="https://www.bbc.com/ukrainian/vert-cul-42924871">[67_BBC_Travel_Corpus_UKR]</a>
    """,

    "7️⃣4️⃣ experience / досвід": 
    
    """
7️⃣4️⃣

💫 <b>experience / досвід</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 209 / частота: 88</i>

🇬🇧 <b>experience</b> - (the process of getting) knowledge or skill from doing, seeing, or feeling things. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"All perception is made up of information from the world and biases we have adjusted from <b>experience</b>."</i> <a href="https://www.bbc.com/future/article/20130701-why-you-feel-phantom-phone-calls">[71_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>досвід</b> - сукупність знань, уміння, які здобуваються в житті, на практиці. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Таким чином наше сприйняття дійсності складається з інформації, яку ми отримуємо з навколишнього світу, та рівня упередженості, якій ми самі скоригували, спираючись на власний <b>досвід</b>."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/02/160205_vert_fut_why_you_feel_phantom_phone_calls_vp">[71_BBC_Future_Corpus_UKR]</a>
    """,

    "7️⃣5️⃣ experiment / експеримент": 
    
    """
7️⃣5️⃣

💫 <b>experiment / експеримент</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 124 / частота: 300</i>

🇬🇧 <b>experiment</b> - a test done in order to learn something or to discover if something works or is true. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Yet dozens of <b>experiments</b> have shown that people are just as likely to report the same symptoms when they are exposed to a sham transmitter that doesn’t actually emit any electromagnetic waves."</i> <a href="https://www.bbc.com/future/article/20150210-can-you-think-yourself-to-death">[47_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>експеримент</b> - один з основних методів наукового дослідження, в якому вивчення явищ відбувається за допомогою доцільно вибраних або штучно створених умов. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Тим не менш, десятки <b>експериментів</b> показали, що люди повідомляють про ті самі симптоми, коли перебувають біля фіктивного пристрою, який насправді не виділяє жодних електромагнітних хвиль."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150707_vert_fut_killing_thoughts_vp">[47_BBC_Future_Corpus_UKR]</a>
    """,

    "7️⃣6️⃣ explain / пояснювати": 
    
    """
7️⃣6️⃣

💫 <b>explain / пояснювати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 238 / частота: 13</i>

🇬🇧 <b>explain</b> - to make something clear or easy to understand by describing or giving information about it. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"The theory is also thought to <b>explain</b> why we seek out and enjoy other intrinsically unpleasant experiences, such as fear-inducing rollercoasters or sad movies."</i> <a href="https://www.bbc.com/future/article/20151001-why-pain-feels-good">[60_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>пояснювати</b> - розповідаючи про що-небудь, робити його ясним, зрозумілим. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Теорія 'доброякісного мазохізму' також <b>пояснює</b>, чому ми прагнемо й інших неприємних відчуттів, не лише фізичних, але й емоційних. Нас так і тягне прокотитися на американських гірках, щоби відчути жах, або подивитися сумний фільм."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151007_vert_fut_why_pain_feels_good_vp">[60_BBC_Future_Corpus_UKR]</a>
    """,

    "7️⃣7️⃣ eye / око": 
    
    """
7️⃣7️⃣

💫 <b>eye / око</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 143 / частота: 76</i>

🇬🇧 <b>eye</b> - one of the two organs in your face that are used for seeing. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"My <b>eyes</b> adjusted to the darkness and a medieval figure took shape – it was St Peter, etched into the wall of New Jerusalem for eternity."</i> <a href="https://www.bbc.com/travel/article/20170817-ethiopias-miraculous-underground-churches">[14_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>око</b> - орган зору у людини, всіх хребетних та деяких безхребетних тварин. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Коли мої <b>очі</b> звикають до темряви, я можу розгледіти середньовічну статую святого Петра, навіки вирізьбленого в стіні Нового Єрусалима."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-42752408">[14_BBC_Travel_Corpus_UKR]</a>
    """,

    "7️⃣8️⃣ face / обличчя": 
    
    """
7️⃣8️⃣

💫 <b>face / обличчя</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 159 / частота: 126</i>

🇬🇧 <b>face</b> - the front of the head, where the eyes, nose, and mouth are. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"This matters because, unfortunately, we can’t resist touching our <b>faces</b>, allowing germs to spread nicely from our hands to our noses and mouths, where they can get into the body."</i> <a href="https://www.bbc.com/future/article/20170519-does-it-matter-how-you-wash-and-dry-your-hands">[18_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>обличчя</b> - передня частина голови людини. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Але це дуже важливо. На жаль, ми не можемо не торкатися нашого <b>обличчя</b>, і таким чином мікроби з рук потрапляють у рот чи ніс, а звідти всередину організму."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-40015296">[18_BBC_Future_Corpus_UKR]</a>
    """,

    "7️⃣9️⃣ fact / факт": 
    
    """
7️⃣9️⃣

💫 <b>fact / факт</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 275 / частота: 151</i>

🇬🇧 <b>fact</b> - something that is known to have happened or to exist, especially something for which proof exists, or about which there is information. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"It’s a scientific <b>fact</b> that high social status is attractive to women. Fertile women prefer more dominant men and the lucky few who achieve money or influence tend to marry younger, more often and have more extra-marital affairs than their peers."</i> <a href=https://www.bbc.com/future/article/20161014-why-billionaires-have-more-sons"">[170_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>факт</b> - дійсна, не вигадана подія, дійсне явище; те, що сталося, відбулося насправді. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Той <b>факт</b>, що високий соціальний статус приваблює жінок, доведений науковцями. Жінки з високою плодючістю віддають перевагу більш домінантним чоловікам – тим, кому пощастило стати багатим і впливовим."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/10/161017_vert_fut_why_billionaires_have_more_sons_vp">[170_BBC_Future_Corpus_UKR]</a>
    """,

    "8️⃣0️⃣ fall / падати": 
    
    """
8️⃣0️⃣

💫 <b>fall / падати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 111 / частота: 17</i>

🇬🇧 <b>fall</b> - to suddenly go down onto the ground or towards the ground without intending to or by accident. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"And of course, shorter people have less distance to <b>fall</b>. According to one estimate, someone who is 20% taller will build up twice as much kinetic energy during a fall."</i> <a href="https://www.bbc.com/future/article/20150928-tall-vs-small-which-is-it-better-to-be">[111_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>падати</b> - переміщатися, валитися, спрямовуватися і т. ін. зверху вниз під дією власної ваги. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Низькі люди й <b>падають</b> з меншої висоти. Згідно з одним дослідженням, 20% різниці у зрості збільшують кінетичну енергію під час падіння в два рази."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150929_vert_fut_tall_vs_small_vp">[111_BBC_Future_Corpus_UKR]</a>
    """,

    "8️⃣1️⃣ family / сім'я": 
    
    """
8️⃣1️⃣

💫 <b>family / сім'я</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 120 / частота: 36</i>

🇬🇧 <b>family</b> - a group of people who are related to each other, such as a mother, a father, and their children. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Every <b>family</b> has several large freezers filled with this rainbow-coloured, large-scaled reef-grazer."</i> <a href="https://www.bbc.com/travel/article/20160412-where-marrying-a-local-is-forbidden">[43_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>сім'я</b> - група людей, що складається з чоловіка, жінки, дітей та інших близьких родичів, які живуть разом. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Кожна <b>сім'я</b> на острові має кілька величезних морозильних камер, наповнених доверху цими барвистими мешканцями рифу."</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/04/160422_vert_tra_where_marrying_a_local_is_forbidden_vp">[43_BBC_Travel_Corpus_UKR]</a>
    """,

    "8️⃣2️⃣ far / далеко": 
    
    """
8️⃣2️⃣

💫 <b>far / далеко</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 261 / частота: 62</i>

🇬🇧 <b>far</b> - at, to, or from a great distance in space or time. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"So it seems we’re least happy at work and most happy when we are <b>farthest</b> from home."</i> <a href="https://www.bbc.com/future/article/20130411-want-to-be-happy-travel-further">[70_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>далеко</b> - який знаходиться, відбувається на великій відстані. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Вчені зробили висновки, що ми почуваємось найменш щасливими на роботі і найбільш задоволеними життям, коли опиняємось <b>далеко</b> від дому."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/01/151230_vert_fut_want_to_be_happy_travel_further_vp">[70_BBC_Future_Corpus_UKR]</a>
    """,

    "8️⃣3️⃣ feel / відчувати": 
    
    """
8️⃣3️⃣

💫 <b>feel / відчувати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 433 / частота: 211</i>

🇬🇧 <b>feel</b> - to experience something physical or emotional. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"If you see red you’ll <b>feel</b> fear and your lower status, and your testosterone will drop,” says Elliot."</i> <a href="https://www.bbc.com/future/article/20140827-how-the-colour-red-warps-the-mind">[90_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>відчувати</b> - переживати якесь почуття. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Коли ми бачимо червоний колір, ми можемо <b>відчувати</b> страх і почуватися більш принижено, що спричиняє зниження рівня тестостерону", – пояснює професор Еліот."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151023_vert_fut_how_the_colour_red_warps_the_mind_vp">[90_BBC_Future_Corpus_UKR]</a>
    """,

    "8️⃣4️⃣ find / знаходити": 
    
    """
8️⃣4️⃣

💫 <b>find / знаходити</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 887 / частота: 43</i>

🇬🇧 <b>find</b> - to discover, especially where a thing or person is, either unexpectedly or by searching, or to discover where to get or how to achieve something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"I can't put it into words how sorry I am," the thief explained. "Please <b>find</b> it in your hearts to forgive the stranger who harmed you."</i> <a href="https://www.bbc.com/travel/article/20150311-can-canada-teach-the-rest-of-us-to-be-nicer">[41_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>знаходити</b> - шукаючи, виявляти кого-, що-небудь десь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Я не можу висловити, як мені шкода, – писав злочинець, який розкаявся. – Будь ласка, спробуйте <b>знайти</b> в вашому серці милосердя і вибачити незнайомця, який заподіяв вам шкоду".</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2015/12/151229_vert_tra_can_canada_teach_the_rest_of_us_to_be_nicer_vp">[41_BBC_Travel_Corpus_UKR]</a>
    """,

    "8️⃣5️⃣ food / їжа": 
    
    """
8️⃣5️⃣

💫 <b>food / їжа</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 240 / частота: 136</i>

🇬🇧 <b>food</b> - something that people and animals eat, or plants absorb, to keep them alive. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"<b>Food</b> was once seen as a source of sustenance and pleasure. Today, the dinner table can instead begin to feel like a minefield."</i> <a href="https://www.bbc.com/future/article/20151029-are-any-foods-safe-to-eat-anymore-heres-the-truth">[108_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>їжа</b> - те, що їдять і п'ють. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Колись давно <b>їжа</b> була джерелом енергії та задоволення. Сьогодні обідній стіл перетворився на справжнє мінне поле."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151215_vert_fut_are_any_foods_safe_to_eat_anymore_heres_the_truth_vp">[108_BBC_Future_Corpus_UKR]</a>
    """,

    "8️⃣6️⃣ friend / друг": 
    
    """
8️⃣6️⃣

💫 <b>friend / друг</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 138 / частота: 33</i>

🇬🇧 <b>friend</b> - a person who you know well and who you like a lot, but who is usually not a member of your family. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Your genes, your <b>friends</b>, the schools you attended, plus many other factors, will all have played a part in making you the person you are today."</i> <a href="https://www.bbc.com/future/article/20160907-clues-to-your-personality-appeared-before-you-could-talk">[144_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>друг</b> - особа, зв'язана з ким-небудь дружбою, довір'ям, відданістю. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Генетична спадковість, <b>друзі</b>, школа, в якій ви вчились, та багато інших факторів зіграли свою роль в становленні тієї людини, якою ви є сьогодні."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/09/160909_vert_fut_personality_child_vp">[144_BBC_Future_Corpus_UKR]</a>
    """,

    "8️⃣7️⃣ future / майбутнє": 
    
    """
8️⃣7️⃣

💫 <b>future / майбутнє</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 156 / частота: 56</i>

🇬🇧 <b>future</b> - what will happen to someone or something in the time that is to come. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"He says he remains optimistic about the <b>future</b> – and the potential for bitcoin to change established ways of using money."</i> <a href="https://www.bbc.com/future/article/20160504-we-looked-inside-a-secret-chinese-bitcoin-mine">[99_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>майбутнє</b> - частина лінії часу, що складається з подій, які ще не відбулися, але відбудуться. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Він каже, що вірить у <b>майбутнє</b> криптовалюти, і що біткойн безперечно змінить те, як ми користуємось грошима сьогодні."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/05/160508_vert_fut_we_looked_inside_a_secret_chinese_bitcoin_mine_vp_rl">[99_BBC_Future_Corpus_UKR]</a>
    """,

    "8️⃣8️⃣ get / отримувати": 
    
    """
8️⃣8️⃣

💫 <b>get / отримувати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 567 / частота: 32</i>

🇬🇧 <b>get</b> - to obtain, buy, or earn something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"I did once <b>get</b> £20 for giving some parents a tiny bowl with a little profiterole to try each after their son refused to let them taste his."</i> <a href="https://www.bbc.com/future/article/20160708-the-mind-tricks-to-get-better-tips">[104_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>отримувати</b> - брати, приймати те, що надсилається, надається, вручається. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Колись я <b>отримала</b> 20 фунтів за те, що принесла батькам крихітне блюдце з профітролями, після того як їхній син не дозволив їм скуштувати профітролі з його тарілки."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/07/160719_vert_fut_the_mind_tricks_to_get_better_tips_vp">[104_BBC_Future_Corpus_UKR]</a>
    """,

    "8️⃣9️⃣ give / давати": 
    
    """
8️⃣9️⃣

💫 <b>give / давати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 401 / частота: 16</i>

🇬🇧 <b>give</b> - to offer something to someone, or to provide someone with something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Reciprocity: you invest with me, and I <b>give</b> you the opportunity of a lifetime – a life so wonderful that no one else can give you something comparable."</i> <a href="https://www.bbc.com/future/article/20160127-the-conman-who-pulled-off-historys-most-audacious-scam">[97_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>давати</b> - передавати від однієї особи до іншої. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Взаємність: ви інвестуєте разом зі мною, а я <b>даю</b> вам можливість, яка з'являється лише раз у житті, ніхто інший не запропонує вам нічого подібного."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/01/160129_vert_most_audacious_scam_vp">[97_BBC_Future_Corpus_UKR]</a>
    """,

    "9️⃣0️⃣ go / піти": 
    
    """
9️⃣0️⃣

💫 <b>go / піти</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 518 / частота: 42</i>

🇬🇧 <b>go</b> - to travel or move to another place. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Or I can <b>go</b> out and exercise before anyone else is up, or talk to people in other time zones."</i> <a href="https://www.bbc.com/future/article/20150706-the-woman-who-barely-sleeps">[30_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>піти</b> - почати пересуватися, рухатися, міняти місце в просторі, ступаючи ногами. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Або я можу <b>піти</b> на прогулянку та зайнятися спортом. Або спілкуватися з людьми в інших часових поясах."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150710_vert_fut_little_sleep_vp">[30_BBC_Future_Corpus_UKR]</a>
    """,

    "9️⃣1️⃣ good / хороший": 
    
    """
9️⃣1️⃣

💫 <b>good / хороший</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 674 / частота: 25</i>

🇬🇧 <b>good</b> - very satisfactory, enjoyable, pleasant, or interesting. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"The Germans obviously appreciate a show of <b>good</b> humour, a fact made evident with the soaring popularity of these comedy venues in Berlin."</i> <a href="https://www.bbc.com/travel/article/20170802-why-people-think-germans-arent-funny">[34_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>хороший</b> - який має позитивні якості або властивості; який своїми якостями цілком відповідає поставленим вимогам. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Німці цінують <b>хороший</b> гумор, і це підтверджує зростаюча останнім часом популярність коміків у Берліні."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-40974629">[34_BBC_Travel_Corpus_UKR]</a>
    """,

    "9️⃣2️⃣ great / чудовий": 
    
    """
9️⃣2️⃣

💫 <b>great / чудовий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 169 / частота: 51</i>

🇬🇧 <b>great</b> - large in amount, size, or degree. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"A <b>great</b> example is the human capacity for echo-location."</i> <a href="https://www.bbc.com/future/article/20141118-how-many-senses-do-you-have">[61_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>чудовий</b> - прекрасний, чудесний. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"<b>Чудовий</b> зразок цього – здатність людини сприймати довколішній світ за допомогою ехолокації."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150917_vert_fut_how_many_senses_do_you_have_vp">[61_BBC_Future_Corpus_UKR]</a>
    """,

    "9️⃣3️⃣ group / група": 
    
    """
9️⃣3️⃣

💫 <b>group / група</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 218 / частота: 207</i>

🇬🇧 <b>group</b> - a number of people or things that are put together or considered as a unit. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"What’s more, when a separate <b>group</b> of participants were shown the stories and asked to judge the traits of the authors, they did a pretty good job, at least for the traits of openness and agreeableness."</i> <a href="https://www.bbc.com/future/article/20170720-the-hidden-ways-your-language-betrays-your-character">[175_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>група</b> - кілька осіб, тварин або предметів, що знаходяться разом, близько один біля одного. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Цікаво, що коли <b>групі</b> випробуваних показали оповідання інших учасників і попросили визначити риси особистості їхніх авторів, вони зробили це досить точно."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-40708690">[175_BBC_Future_Corpus_UKR]</a>
    """,

    "9️⃣4️⃣ grow / рости": 
    
    """
9️⃣4️⃣

💫 <b>grow / рости</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 127 / частота: 22</i>

🇬🇧 <b>grow</b> - to increase in size or amount, or to become more advanced or developed. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Bald men are genetically more predisposed to be more sensitive to dihydrotestosterone, but the follicles on the chin are unaffected by the hormone, which is why beards continue to <b>grow</b>."</i> <a href="https://www.bbc.com/future/article/20121210-are-bald-men-more-virile">[95_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>рости</b> - ставати більшим на зріст, довшим, вищим, збільшуватися в результаті життєвого процесу. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Фолікули на голові лисих чоловіків генетично більш чутливі до дигідротестостерону, але цей гормон не руйнує фолікули на підборідді, тому борода продовжує <b>рости</b>."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151217_vert_fut_are_bald_men_more_virile_vp">[95_BBC_Future_Corpus_UKR]</a>
    """,

    "9️⃣5️⃣ hand / рука": 
    
    """
9️⃣5️⃣

💫 <b>hand / рука</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 218 / частота: 186</i>

🇬🇧 <b>hand</b> - the part of the body at the end of the arm that is used for holding, moving, touching, and feeling things. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"We humans don’t typically agree on all that much, but there is at least one thing that an impressive amount of us accept: which <b>hand</b> is easiest to control."</i> <a href="https://www.bbc.com/future/article/20141215-why-are-most-of-us-right-handed">[122_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>рука</b> - кожна з двох верхніх кінцівок людини від плечового суглоба до кінчиків пальців. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Нам, людям, зазвичай доволі важко дійти згоди у багатьох питаннях, але є, принаймні, одна річ, з якою більшість неодмінно погодиться: якою <b>рукою</b> нам легше виконувати точні та складні дії."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/02/160218_vert_fut_why_are_most_of_us_right_handed_vp">[122_BBC_Future_Corpus_UKR]</a>
    """,

    "9️⃣6️⃣ happen / траплятися": 
    
    """
9️⃣6️⃣

💫 <b>happen / траплятися</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 192 / частота: 51</i>

🇬🇧 <b>happen</b> - (of a situation or an event) to have existence or come into existence. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"It isn't that these are the only things that <b>happen</b>. Perhaps journalists are drawn to reporting bad news because sudden disaster is more compelling than slow improvements."</i> <a href="https://www.bbc.com/future/article/20140728-why-is-all-the-news-bad">[81_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>траплятися</b> - відбуватися, діятися, ставатися. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Звичайно, в світі <b>трапляється</b> не лише погане. Втім, можливо, повідомлення про катастрофи є більш переконливими, ніж новини про повільні зміни на краще."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151217_vert_fut_why_is_all_the_news_bad_vp">[81_BBC_Future_Corpus_UKR]</a>
    """,

    "9️⃣7️⃣ have / мати": 
    
    """
9️⃣7️⃣

💫<b>have / мати</b>💫

🔹<i>verb / дієслово</i>
🔹<i>frequency: 3606 / частота: </i>

🇬🇧 <b>have</b> - to own. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Portugal’s “joyful sadness” is encapsulated in a single word: saudade. No other language <b>has</b> a word quite like it.</i> <a href="https://www.bbc.com/travel/article/20161118-the-european-country-that-loves-being-sad">[21_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>мати</b> - уживається на означення того, що комусь належить що-небудь, є його власністю. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Солодка меланхолія" португальців втілюється в одному слові: saudade. Жодна інша мова не <b>має</b> схожого слова.</i> <a href="https://www.bbc.com/ukrainian/vert-cap-38161263">[21_BBC_Travel_Corpus_UKR]</a>
    """,

    "9️⃣8️⃣ he / він": 
    
    """
9️⃣8️⃣

💫 <b>he / він</b> 💫

🔹 <i>pronoun / займенник</i>
🔹 <i>frequency: 1357 / частота: 976</i>

🇬🇧 <b>he</b> - used as the subject of a verb to refer to a man, boy, or male animal that has already been mentioned. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"<b>He</b> was a successful father and military officer with good job evaluations,” says Burgess. “There was no reason to think that there was anything wrong psychiatrically."</i> <a href="https://www.bbc.com/future/article/20150630-my-dentist-saved-my-tooth-but-stole-my-memory">[45_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>він</b> - уживається на означення предмета мовлення, вираженого іменником чоловічого роду однини в попередньому реченні або після цього займенника. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"<b>Він</b> був гарним батьком і його поважали на службі, – каже доктор Берджес. – Немає жодних причин вважати, що він мав якісь психіатричні ускладнення".</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150820_vert_fut_dentist_extracted_memory_vp">[45_BBC_Future_Corpus_UKR]</a>
    """,

    "9️⃣9️⃣ head / голова": 
    
    """
9️⃣9️⃣

💫 <b>head / голова</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 139 / частота: 81</i>

🇬🇧 <b>head</b> - the part of the body above the neck where the eyes, nose, mouth, ears, and brain are. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"If you wiggle your <b>head</b> around while reading, for example, you’ll see that it makes little difference to your ability to read and stay focused on the words."</i> <a href="https://www.bbc.com/future/article/20141118-how-many-senses-do-you-have">[61_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>голова</b> - частина тіла людини або тварини, в якій міститься мозок. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Якщо ви легко похитаєте <b>головою</b> під час читання, то помітите, що ці рухи майже не впливають на вашу здатність читати і зосереджуватися на словах."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150917_vert_fut_how_many_senses_do_you_have_vp">[61_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣0️⃣0️⃣ health / здоров'я": 
    
    """
1️⃣0️⃣0️⃣

💫 <b>health / здоров'я</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 144 / частота: 135</i>

🇬🇧 <b>health</b> - the condition of the body and the degree to which it is free from illness, or the state of being well. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Overwhelming evidence shows the excessive consumption of sugar leads to all kinds of <b>health</b> problems, including diabetes and heart disease."</i> <a href="https://www.bbc.com/future/article/20161125-the-true-costs-of-our-favourite-foods">[06_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>здоров'я</b> - стан організму, при якому нормально функціонують усі його органи. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Безліч досліджень невблаганно підтверджують, що надмірне споживання цукру призводить до багатьох проблем зі <b>здоров'ям</b>, зокрема діабету і серцево-судинних захворювань."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-38131971">[06_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣0️⃣1️⃣ hear / чути": 
    
    """
1️⃣0️⃣1️⃣

💫 <b>hear / чути</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 109 / частота: 62</i>

🇬🇧 <b>hear</b> - to receive or become conscious of a sound using your ears. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"But it was hard to <b>hear</b> him over the machine’s steady tick and spinning gears."</i> <a href="https://www.bbc.com/travel/article/20160901-the-clock-that-changed-the-meaning-of-time">[01_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>чути</b> - сприймати звукові коливання за допомогою органів слуху. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Його погано <b>чути</b> через постійне цокання механізму і обертання коліщат."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-38531366">[01_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣0️⃣2️⃣ heart / серце": 
    
    """
1️⃣0️⃣2️⃣

💫 <b>heart / серце</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 129 / частота: 66</i>

🇬🇧 <b>heart</b> - the organ in your chest that sends the blood around your body. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Your <b>heart</b> is an incredibly hardworking organ. In five minutes, it will pump five litres of blood around your body."</i> <a href="https://www.bbc.com/future/article/20160520-the-incredible-things-we-know-about-your-heart-and-blood">[162_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>серце</b> - центральний орган кровоносної системи у вигляді м'язового мішка, ритмічні скорочення якого забезпечують кровообіг. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Наше <b>серце</b> – це неймовірно працьовитий орган. Упродовж п'яти хвилин воно прокачує п'ять літрів крові."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/05/160524_vert_fut_things_we_know_about_your_heart_and_blood_vp">[162_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣0️⃣3️⃣ help / допомагати": 
    
    """
1️⃣0️⃣3️⃣

💫 <b>help / допомагати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 344 / частота: 139</i>

🇬🇧 <b>help</b> - to make it possible or easier for someone to do something, by doing part of the work yourself or by providing advice, money, support, etc. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"On the plus side, red clothes might also <b>help</b> you to perform better in an interview. Some fashion experts suggest red ties project authority and dominance in the workplace, as BBC Capital explained this week."</i> <a href="https://www.bbc.com/future/article/20140827-how-the-colour-red-warps-the-mind">[90_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>допомагати</b> - подавати допомогу кому-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"З іншого боку, червоний одяг може <b>допомогти</b> вам краще пройти співбесіду на роботу. Деякі експерти вважають, що червона краватка допоможе вам продемонструвати впевненість в компетентність під час інтерв'ю."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151023_vert_fut_how_the_colour_red_warps_the_mind_vp">[90_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣0️⃣4️⃣ here / тут": 
    
    """
1️⃣0️⃣4️⃣

💫 <b>here / тут</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 162 / частота: 216</i>

🇬🇧 <b>here</b> - in, at, or to this place. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Many of us long-term locals have noticed that either you love Vegas and you thrive <b>here</b>, or it chews you up and spits you out,” he said."</i> <a href="https://www.bbc.com/travel/article/20170917-the-surprising-side-to-las-vegas-that-few-know">[12_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>тут</b> - у цьому місці. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Ті з нас, хто живе <b>тут</b> давно, вже помітили: або тобі подобається у Вегасі і ти <b>тут</b> процвітаєш, або це місто пожує тебе і виплюне."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-44266837">[12_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣0️⃣5️⃣ history / історія":

    """
1️⃣0️⃣5️⃣

💫 <b>history / історія</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 130 / частота: 260</i>

🇬🇧 <b>history</b> - (the study of or a record of) past events considered together, especially events of a particular period, country, or subject. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Many travellers tend to seek attractions of the manmade variety: art and architecture, food and music, <b>history</b> and culture."</i> <a href="https://www.bbc.com/travel/article/20140903-surreal-towns-shaped-by-nature">[35_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>історія</b> - процес розвитку, зміна чого-небудь; події в процесі життя народу, його певної частини тощо. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Більшість мандрівників вирушають у подорож в пошуках рукотворних пам'яток: мистецтва і архітектури, їжі та музики, <b>історії</b> та культури."</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/06/160603_vert_tra_surreal_towns_shaped_by_nature_vp">[35_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣0️⃣6️⃣ hold / тримати":

    """
1️⃣0️⃣6️⃣

💫 <b>hold / тримати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 108 / частота: 54</i>

🇬🇧 <b>hold</b> - to take and keep something in your hand or arms. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"When people get to the stage where their arms aren’t long enough to <b>hold</b> a book or menu far enough away to focus on the text, they opt for reading glasses."</i> <a href="https://www.bbc.com/future/article/20140513-do-glasses-weaken-your-eyesight">[182_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>тримати</b> - взявши що-небудь у руки, в рот, у зуби тощо, ухопившись за щось, не випускати, мати в руках, у зубах тощо. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Коли довжини рук вже не вистачає, щоб <b>тримати</b> книжку або меню достатньо далеко від очей, людина надягає окуляри для читання."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/06/160624_vert_fut_do_spectacles_worsen_sight_vp">[182_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣0️⃣7️⃣ home / дім":

    """
1️⃣0️⃣7️⃣

💫 <b>home / дім</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 157 / частота: 33</i>

🇬🇧 <b>home</b> - the house, apartment, etc. where you live, especially with your family. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"And seven years on, I am beginning to accept that <b>home</b> is a shapeshift thing, belonging is just as elusive, and the country that raised me is an imaginary land that once was, and is no more, except in our collective memory."</i> <a href="https://www.bbc.com/travel/article/20180425-im-from-a-country-that-no-longer-exists">[65_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>дім</b> - приміщення, люди, що в ньому живуть, та їх господарство. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Сім років по тому я поступово починаю миритися з тим, що <b>дім</b> - це те, що змінюється. Почуття приналежності теж важко вловиме, а країна, де я виросла, залишилася існувати тільки в моїй уяві. Її більше немає - якщо не брати до уваги нашої колективної пам'яті."</i> <a href="https://www.bbc.com/ukrainian/features-44100405">[65_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣0️⃣8️⃣ hour / година":

    """
1️⃣0️⃣8️⃣

💫 <b>hour / година</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 196 / частота: 163</i>

🇬🇧 <b>hour</b> - a period of 60 minutes. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Tourism will always be there and tourists don’t care. The number of <b>hours</b> of sunlight will be the same, whether it is an extra hour in the morning or in the evening."</i> <a href="https://www.bbc.com/travel/article/20170504-the-strange-reason-spaniards-eat-late">[20_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>година</b> - одиниця виміру часу, що дорівнює 1/24 доби, або 60 хвилинам. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Туристи нікуди не зникнуть, адже для них це не має значення. Та й кількість <b>годин</b> сонячного світла лишиться такою самою, хіба що додаткова година сонячного світла з'явиться вранці."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-39849128">[20_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣0️⃣9️⃣ house / будинок":

    """
1️⃣0️⃣9️⃣

💫 <b>house / будинок</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 111 / частота: 113</i>

🇬🇧 <b>house</b> - a building that people, usually one family, live in. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"If you have a <b>house</b>, don’t maintain a lawn, let native plants take over and grow taller. Cut them once or twice a year."</i> <a href="https://www.bbc.com/future/article/20151118-can-you-be-too-clean">[142_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>будинок</b> - будівля, споруда, призначена для житла. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Якщо у вас є <b>будинок</b>, не треба постійно доглядати за газоном, дозвольте диким рослинам розростися на ньому. Ви можете підстригати їх всього один або два рази на рік."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/11/151125_vert_fut_can_you_be_too_clean_vp">[142_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣1️⃣0️⃣ human / людина":

    """
1️⃣1️⃣0️⃣

💫 <b>human / людина</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 285 / частота: 903</i>

🇬🇧 <b>human</b> - a person. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Overall, the jury is out on just how long a <b>human</b> could ever stay awake, but perhaps that's a good thing."</i> <a href="https://www.bbc.com/future/article/20150220-how-long-can-we-stay-awake">[176_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>людина</b> - людська постать. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Тож питання про те, скільки часу <b>людина</b> може провести без сну, досі відкрите. Але, може, це й на краще."</i> <a href="https://www.bbc.com/ukrainian/vert-earth-41231270">[176_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣1️⃣1️⃣ I / я":

    """
1️⃣1️⃣1️⃣

💫 <b>I / я</b> 💫

🔹 <i>pronoun / займенник</i>
🔹 <i>frequency: 1637 / частота: 1217</i>

🇬🇧 <b>I</b> - used as the subject of a verb to refer to the person speaking or writing. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"<b>I</b> love you not only for what you are, but for what <b>I</b> am when I am with you. <b>I</b> love you not only for what you have made of yourself, but for what you are making of me."</i> <a href="https://www.bbc.com/future/article/20161205-how-break-ups-change-your-personality">[22_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>я</b> - вживається мовцем для називання самого себе. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"<b>Я</b> кохаю тебе не тільки за те, ким ти є, але й за те, ким <b>я</b> є поруч з тобою. <b>Я</b> кохаю тебе не тільки за те, ким ти став, але й за те, ким ти зробив мене."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-38241503">[22_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣1️⃣2️⃣ idea / ідея":

    """
1️⃣1️⃣2️⃣

💫 <b>idea / ідея</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 252 / частота: 161</i>

🇬🇧 <b>idea</b> - a suggestion or plan for doing something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"One of these is the <b>idea</b> that the human brain is served by five senses."</i> <a href="https://www.bbc.com/future/article/20141118-how-many-senses-do-you-have">[61_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>ідея</b> - поняття, уявлення, що відбивають дійсність у свідомості людини та виражають ставлення її до навколишнього світу. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Одним із таких фактів є <b>ідея</b> про те, що мозок людини сприймає рівно п'ять чуттів – ні більше, ні менше."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150917_vert_fut_how_many_senses_do_you_have_vp">[61_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣1️⃣3️⃣ important / важливий":

    """
1️⃣1️⃣3️⃣

💫 <b>important / важливий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 165 / частота: 156</i>

🇬🇧 <b>important</b> - necessary or of great value. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Every page, every <b>important</b> fact, evokes a comforting feeling of familiarity."</i> <a href="https://www.bbc.com/future/article/20140917-the-worst-way-to-learn">[193_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>важливий</b> - який має велике, особливе значення. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Кожна сторінка, кожен <b>важливий</b> факт і термін виглядають заспокійливо знайомими."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-39933997">[193_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣1️⃣4️⃣ include / включати":
    
    """
1️⃣1️⃣4️⃣

💫 <b>include / включати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 216 / частота: 19</i>

🇬🇧 <b>include</b> - to contain something as a part of something else, or to make something part of something else. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"The list of allergens <b>includes</b> – but is not limited to – latex, gold, pollen (ragweed, cockleweed and pigweed are especially bad), penicillin, insect venom, peanuts, papayas, jellyfish stings, perfume, eggs, the faeces of house mites, pecans, salmon, beef and nickel."</i> <a href="https://www.bbc.com/future/article/20150409-why-do-we-have-allergies">[138_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>включати</b> - уводити до складу, приєднувати до кого-, чого-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Найпоширеніші алергени <b>включають</b> латекс, золото, пилок рослин (амброзія, пажитниця і щириця є особливо небезпечними), пеніцилін, отруту комах, арахіс, папайю, опіки від медуз, парфуми, яйця, фекалії домашніх кліщів, горіхи пекан, сьомгу, яловичину та нікель. Але цей список далеко неповний."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/08/160817_vert_fut_why_do_we_have_allergies_vp">[138_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣1️⃣5️⃣ increase / збільшувати":
    
    """
1️⃣1️⃣5️⃣

💫 <b>increase / збільшувати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 135 / частота: 12</i>

🇬🇧 <b>increase</b> - to (make something) become larger in amount or size. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"We can <b>increase</b> the profits of a restaurant by thousands simply by rearranging the items on the menu."</i> <a href="https://www.bbc.com/future/article/20171120-the-secret-tricks-hidden-inside-restaurant-menus">[103_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>збільшувати</b> - робити більшим за кількістю, розміром, тривалістю і т. ін. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Можна <b>збільшити</b> прибуток ресторану на тисячі доларів, просто переставивши позиції в меню."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-42100075">[103_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣1️⃣6️⃣ individual / індивідуальний":
    
    """
1️⃣1️⃣6️⃣

💫 <b>individual / індивідуальний</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 56 / частота: 13</i>

🇬🇧 <b>individual</b> - existing and considered separately from the other things or people in a group. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Pick-and-mix religious beliefs are not new. But it is easier than ever to fashion an <b>individualised</b> faith."</i> <a href="https://www.bbc.com/future/article/20170222-how-smartphones-and-social-media-are-changing-religion">[116_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>індивідуальний</b> - властивий певній особі. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Такий підхід до віри, звісно, не новий. Але сьогодні - легше, ніж будь-коли, виробити свій <b>індивідуальний</b> шлях у духовність."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-39082655">[116_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣1️⃣7️⃣ influence / впливати":
    
    """
1️⃣1️⃣7️⃣

💫 <b>influence / впливати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 102 / частота: 216</i>

🇬🇧 <b>influence</b> - to affect or change how someone or something develops, behaves, or thinks. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"If fake news stories about politics can <b>influence</b> voting patterns, then could health stories about unproven treatments result in people eschewing their current medical treatment in favour of the latest recommendation in an article they see?"</i> <a href="https://www.bbc.com/future/article/20170207-how-to-spot-misleading-health-news">[03_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>впливати</b> - діяти певним чином на кого-, що-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Якщо фейкові політичні новини можуть <b>вплинути</b> на голоси виборців, чи не змусить нас оманлива медична інформація в інтернеті відмовлятися від прописаного лікування на користь неперевірених порад?"</i> <a href="https://www.bbc.com/ukrainian/vert-fut-38968836">[03_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣1️⃣8️⃣ information / інформація":
    
    """
1️⃣1️⃣8️⃣

💫 <b>information / інформація</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 115 / частота: 153</i>

🇬🇧 <b>information</b> - facts about a situation, person, event, etc. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"All perception is made up of <b>information</b> from the world and biases we have adjusted from experience."</i> <a href="https://www.bbc.com/future/article/20130701-why-you-feel-phantom-phone-calls">[71_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>інформація</b> - відомості про які-небудь події, чиюсь діяльність і т. ін.; повідомлення про щось. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Таким чином наше сприйняття дійсності складається з <b>інформації</b>, яку ми отримуємо з навколишнього світу, та рівня упередженості, якій ми самі скоригували, спираючись на власний досвід."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/02/160205_vert_fut_why_you_feel_phantom_phone_calls_vp">[71_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣1️⃣9️⃣ instead / натомість":
    
    """
1️⃣1️⃣9️⃣

💫 <b>instead / натомість</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 119 / частота: 7</i>

🇬🇧 <b>instead</b> - in place of someone or something else. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"<b>Instead</b>, she believes his grammar and sentence construction indicate that Catalan was his native language."</i> <a href="https://www.bbc.com/travel/article/20121107-the-mystery-of-christopher-columbuss-legacy">[75_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>натомість</b> - замість чого-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"<b>Натомість</b>, вчена впевнена, що судячи з граматичних конструкцій і будови речень, які він вживав, рідною мовою мореплавця була каталонська."</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/02/160202_vert_tra_the_mystery_of_christopher_columbuss_legacy_vp">[75_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣2️⃣0️⃣ involve / полягати":
    
    """
1️⃣2️⃣0️⃣

💫 <b>involve / полягати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 109 / частота: 69</i>

🇬🇧 <b>involve</b> - if an activity, situation, etc. involves something, that thing is a part of the activity, etc. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"A similar, but distinct, tactic might <b>involve</b> putting yourself in someone else’s shoes and imagining their viewpoint."</i> <a href="https://www.bbc.com/future/article/20150422-how-not-to-be-stupid">[35_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>полягати</b> - зводитися до чого-небудь, мати своєю суттю, своїм змістом щось. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Аналогічна тактика <b>полягає</b> в тому, щоби уявити себе на місці іншої людини і спробувати зрозуміти її точку зору."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151020_vert_fut_how_not_to_be_stupid_vp">[35_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣2️⃣1️⃣ island / острів":
    
    """
1️⃣2️⃣1️⃣

💫 <b>island / острів</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 147 / частота: 182</i>

🇬🇧 <b>island</b> - a piece of land completely surrounded by water. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Though tiny, the <b>island</b> has played an outsize role in history. It was the site of the Ni’ihau Incident in 1941, when, following the attack on Pearl Harbor, a Japanese navy fighter pilot crashed on the <b>island</b> and terrorized its residents for a week."</i> <a href="https://www.bbc.com/travel/article/20160225-the-worlds-most-secretive-places">[06_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>острів</b> - ділянка суші, оточена з усіх боків водою. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Попри свій крихітний розмір, <b>острів</b> зіграв неабияку роль в історії. Саме тут 1941 року, після атаки на Перл-Гарбор, розбився японський винищувач, пілот якого протягом тижня тероризував місцевих жителів."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-40557407">[06_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣2️⃣2️⃣ it / воно":
    
    """
1️⃣2️⃣2️⃣

💫 <b>it / воно</b> 💫

🔹 <i>pronoun / займенник</i>
🔹 <i>frequency: 4127 / частота: 89</i>

🇬🇧 <b>it</b> - used as the subject of a verb, or the object of a verb or preposition, to refer to a thing, animal, situation, or idea that has already been mentioned. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"<b>It</b> also offers a good basis for how language gets transmitted between cultures, often mutating in the process."</i> <a href="https://www.bbc.com/future/article/20120427-when-is-a-colour-not-a-colour">[94_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>воно</b> - займенник, що використовується для позначення предмета, тварини, ситуації або ідеї, яка вже була згадана. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"<b>Воно</b> також допомагає зрозуміти, як культури взаємодіють через мови і як мови змінюються в цьому процесі."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151216_vert_fut_when_is_a_colour_not_a_colour_vp">[94_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣2️⃣3️⃣ just / просто":

    """
1️⃣2️⃣3️⃣

💫 <b>just / просто</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 654 / частота: 207</i>

🇬🇧 <b>just</b> - only; simply. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"We asked them to imagine meeting a friend next weekend – and they <b>just</b> couldn’t do it.” The same was true when they were asked to imagine a future visit to the seaside."</i> <a href="https://www.bbc.com/future/article/20150225-secrets-of-alice-in-wonderland">[46_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>просто</b> - тільки, лише. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Ми попросили їх уявити зустріч з другом наступного тижня – і вони <b>просто</b> не могли це зробити", - каже науковець. Ці люди також не могли уявити майбутню подорож до моря."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150708_vert_fut_alice_in_wonderland_psychology_vp">[46_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣2️⃣4️⃣ keep / тримати":

    """
1️⃣2️⃣4️⃣

💫 <b>keep / тримати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 171 / частота: 54</i>

🇬🇧 <b>keep</b> - to continue doing something without stopping, or to do it repeatedly. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"You sit in a restaurant with a friend and they will happily, in a room full of strangers, talk quite loudly about their medical problems or their parents’ divorce or their love life. They see no reason to <b>keep</b> it a secret."</i> <a href="https://www.bbc.com/travel/article/20180131-where-dutch-directness-comes-from">[64_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>тримати</b> - змушувати когось, щось перебувати в якому-небудь положенні, стані. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Сидячи в ресторані, повному незнайомих людей, вони можуть голосно розповідати про свої проблеми зі здоров'ям або про розлучення батьків чи любовні стосунки. Вони не бачать причин <b>тримати</b> це в таємниці."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-43128149">[64_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣2️⃣5️⃣ kind / добрий":

    """
1️⃣2️⃣5️⃣

💫 <b>kind / добрий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 154 / частота: 10</i>

🇬🇧 <b>kind</b> - generous, helpful, and thinking about other people's feelings. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"The personality test asked participants to rate how accurately 100 different trait adjectives described their personalities, including words such as bashful, <b>kind</b>, neat, relaxed, moody, bright and artistic."</i> <a href="https://www.bbc.com/future/article/20170518-the-everyday-habits-that-reveal-our-personalities">[19_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>добрий</b> - який доброзичливо, приязно, чуйно ставиться до людей. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Під час тесту учасників попросили охарактеризувати свою особистість за допомогою 100 різних прикметників, як-от сором'язливий, <b>добрий</b>, акуратний, спокійний, примхливий, яскравий і артистичний."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-39972917">[19_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣2️⃣6️⃣ know / знати":

    """
1️⃣2️⃣6️⃣

💫 <b>know / знати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 613 / частота: 196</i>

🇬🇧 <b>know</b> - to have information in your mind. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"You can leave your bag at the table at any restaurant and go to the cashier to order food with the peace of mind that your bag will still be there,” she said. “Residents <b>know</b> that there is a high chance of being caught and punished."</i> <a href="https://www.bbc.com/travel/article/20150529-living-in-the-worlds-safest-cities">[68_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>знати</b> - мати якісь дані, відомості про кого-, що-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Ви можете спокійно залишити сумку на столику в ресторані, якщо вам потрібно розрахуватися на касі, - розповідає Ванджрі Раві. - Місцеві чудово <b>знають</b>, що шанс бути спійманим і покараним дуже високий".</i> <a href="https://www.bbc.com/ukrainian/vert-tra-40521665">[68_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣2️⃣7️⃣ language / мова":
    
    """
1️⃣2️⃣7️⃣

💫 <b>language / мова</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 486 / частота: 638</i>

🇬🇧 <b>language</b> - a system of communication consisting of sounds, words, and grammar. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"And for expats whose first <b>language</b> is not English, this will speed up their language skills."</i> <a href="https://www.bbc.com/travel/article/20160428-the-irish-city-that-won-facebook">[36_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>мова</b> - сукупність довільно відтворюваних загальноприйнятих у межах даного суспільства звукових знаків для об'єктивно існуючих явищ і понять, а також загальноприйнятих правил їх комбінування у процесі вираження думок. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"До того ж, якщо англійська не є вашою рідною <b>мовою</b>, життя в центрі столиці прискорить її опанування."</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/05/160504_vert_tra_the_irish_city_that_won_facebook_vp">[36_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣2️⃣8️⃣ large / великий":
    
    """
1️⃣2️⃣8️⃣

💫 <b>large / великий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 157 / частота: 306</i>

🇬🇧 <b>large</b> - big in size or amount. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"The islands – which range from <b>large</b> and inhabited to rocky outposts and knolls – were carved by glaciers moving across the landscape thousands of years ago, leaving enormous pieces of granite behind."</i> <a href="https://www.bbc.com/travel/article/20140903-surreal-towns-shaped-by-nature">[35_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>великий</b> - значний своїми розмірами, величиною. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Острови, які варіюються від <b>великих</b> і заселених до непридатних для життя маленьких скель, було створено льодовиками, що мандрували тут тисячі років тому і залишили величезні уламки граніту."</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/06/160603_vert_tra_surreal_towns_shaped_by_nature_vp">[35_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣2️⃣9️⃣ lead / призводити":
    
    """
1️⃣2️⃣9️⃣

💫 <b>lead / призводити</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 198 / частота: 54</i>

🇬🇧 <b>lead</b> - to influence someone to do something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Two possible mechanisms have been proposed to explain why leg-crossing might <b>lead</b> to a temporary rise in blood pressure."</i> <a href="https://www.bbc.com/future/article/20151013-is-crossing-your-legs-bad-for-you">[59_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>призводити</b> - доводити кого-небудь до якогось стану. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Два механізми можуть пояснити, чому закидання ноги на ногу може <b>призвести</b> до тимчасового підвищення артеріального тиску."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151015_vert_fut_is_crossing_your_legs_bad_for_you_vp">[59_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣3️⃣0️⃣ learn / вивчати":
    
    """
1️⃣3️⃣0️⃣

💫 <b>learn / вивчати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 283 / частота: 136</i>

🇬🇧 <b>learn</b> - to get new knowledge or skill in a subject or activity. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"'At this age, children don’t <b>learn</b> a language – they acquire it,' says the school’s director Carmen Rampersad."</i> <a href="https://www.bbc.com/future/article/20181024-the-best-age-to-learn-a-foreign-language">[133_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>вивчати</b> - навчаючись, набувати певних знань, відомостей в якій-небудь галузі; опановувати щось. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"'У цьому віці діти не <b>вивчають</b> мову - вони її набувають', - каже директорка садку Кармен Рамперсад."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-45997320">[133_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣3️⃣1️⃣ level / рівень":

    """
1️⃣3️⃣1️⃣

💫 <b>level / рівень</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 128 / частота: 202</i>

🇬🇧 <b>level</b> - the height of something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"One way of accounting for this is to assume that lottery winners get used to their new <b>level</b> of wealth, and simply adjust back to a baseline level of happiness – something called the ‘hedonic treadmill’."</i> <a href="https://www.bbc.com/future/article/20130326-why-money-cant-buy-you-happiness">[101_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>рівень</b> - ступінь якості, величина і т. ін., досягнуті у чому-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Одне з пояснень – те, що переможці лотерей звикають до нового матеріального стану і вертаються на базовий <b>рівень</b> щастя – так звану 'гедоністичну бігову доріжку'."</i> <a href="https://www.bbc.com/ukrainian/vert_cap/2016/07/160718_vert_cap_why_money_cant_buy_you_happiness_vp">[101_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣3️⃣2️⃣ life / життя":
    
    """
1️⃣3️⃣2️⃣

💫 <b>life / життя</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 460 / частота: 574</i>

🇬🇧 <b>life</b> - the period between birth and death, or the experience or state of being alive. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Built from pH-neutral marine cement, his sculptures are meant to represent the relationship between humans and nature, and on a deeper level, the harmony between <b>life</b> and art."</i> <a href="https://www.bbc.com/travel/article/20160205-europes-first-underwater-museum-opens">[38_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>життя</b> - існування всього живого. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Всі його скульптури, створені з морського цементу з нейтральним рівнем рН, символізують відносини між людиною і природою, і – на більш глибокому рівні – гармонію між <b>життям</b> і мистецтвом."</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/02/160209_vert_tra_europes_first_underwater_museum_opens_vp">[38_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣3️⃣3️⃣ like / подобатися":
    
    """
1️⃣3️⃣3️⃣

💫 <b>like / подобатися</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 880 / частота: 76</i>

🇬🇧 <b>like</b> - to enjoy or approve of something or someone. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>""If you don't  <b>like</b> them you can just go separate ways,' he wrote. 'No need to stick with people you don't like. After all, it's your adventure!""</i> <a href="https://www.bbc.com/travel/article/20150831-why-you-should-travel-solo">[47_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>подобатися</b> - викликати симпатію, прихильність до кого-небудь; справляти на когось приємне враження. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>""Якщо людина вам не  <b>сподобається</b>, ви просто розійдетесь,' – пише він. 'Вас же ніхто не змушує товаришувати з тим, хто вам не подобається. Зрештою, це ж ваша пригода!""</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/03/160302_vert_tra_why_you_should_travel_solo_vp">[47_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣3️⃣4️⃣ line / лінія":

    """
1️⃣3️⃣4️⃣

💫 <b>line / лінія</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 112 / частота: 19</i>

🇬🇧 <b>line</b> - a long, thin mark on the surface of something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"In addition to losing the new islands, they now had no room to manoeuver when embarking on their voyages to Africa as the <b>line</b> ran only 100 leagues (about 320 miles) west of Cape Verde."</i> <a href="https://www.bbc.com/travel/article/20170615-the-town-that-split-the-world-in-two">[11_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>лінія</b> - смуга, справжня або уявна, яка визначає межу, границю чого-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Вони втрачали не лише нові острови, але й територію для маневрів під час подорожей до Африки - <b>лінія</b> розмежування пролягала за 320 миль на захід від Кабо-Верде."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-43729118">[11_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣3️⃣5️⃣ live / жити":

    """
1️⃣3️⃣5️⃣

💫 <b>live / жити</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 379 / частота: 141</i>

🇬🇧 <b>live</b> - (to continue) to be alive or have life. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"And although I may complain about Dutch directness, I’m grateful to <b>live</b> in a country that allows me to be just that."</i> <a href="https://www.bbc.com/travel/article/20180131-where-dutch-directness-comes-from">[64_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>жити</b> - бути живим, існувати. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"І хоча я все ще звикаю до цієї традиції рубати все з плеча, я вдячна, що <b>живу</b> в країні, де можу завжди бути щирою."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-43128149">[64_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣3️⃣6️⃣ long / довгий":
    
    """
1️⃣3️⃣6️⃣

💫 <b>long / довгий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 411 / частота: 87</i>

🇬🇧 <b>long</b> - being a distance between two points that is more than average or usual. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"He identified among the many factors associated with <b>long</b> life: a moderate diet that was rich in vegetables and short on meat and sweetened pastries; an active lifestyle; good care of your teeth; weekly bathing in lukewarm water with soap; good sleep; clean air; and being born to parents who themselves lived long lives."</i> <a href="https://www.bbc.com/future/article/20140421-how-to-live-forever">[113_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>довгий</b> - який має велику довжину. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Серед багатьох чинників, пов'язаних з <b>довгим</b> життям, від називає помірну дієту, в якій багато овочів та мало м'яса і солодкої випічки, рухливість, хороший догляд за зубами, купання в теплій воді з милом щотижня, хороший сон, чисте повітря і батьків, які самі жили довго."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150806_vert_fut_how_to_live_forever_vp">[113_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣3️⃣7️⃣ look / подивитися": 
    
    """
1️⃣3️⃣7️⃣

💫 <b>look / подивитися</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 400 / частота: 47</i>

🇬🇧 <b>look</b> - to direct your eyes in order to see. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Customers like to interact with the product, especially fresh food, so they can <b>look</b> at it and check it,” says retail commentator Clare Rayner."</i> <a href="https://www.bbc.com/future/article/20150804-shop-but-dont-enter-the-strange-world-of-dark-stores">[78_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>подивитися</b> - спрямувати погляд у певному напрямку на кого-, що-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Клієнтам подобається взаємодіяти з продуктами, особливо свіжими, бо вони можуть <b>подивитися</b> на них, помацати, перевірити", – говорить консультант з роздрібної торгівлі Клер Рейнер."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150817_vert_shop_but_dont_enter_vp">[78_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣3️⃣8️⃣ love / кохати": 
    
    """
1️⃣3️⃣8️⃣

💫 <b>love / кохати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 103 / частота: 7</i>

🇬🇧 <b>love</b> - to like another adult very much and be romantically and sexually attracted to them, or to have strong feelings of liking a friend or person in your family. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"I <b>love</b> you for the part of me that you bring out."</i> <a href="https://www.bbc.com/future/article/20161205-how-break-ups-change-your-personality">[22_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>кохати</b> - почувати, виявляти глибоку сердечну прихильність до особи іншої статі. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Я <b>кохаю</b> тебе за ту частину мене, яку ти відкрив."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-38241503">[22_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣3️⃣9️⃣ low / низький":

    """
1️⃣3️⃣9️⃣

💫 <b>low / низький</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 136 / частота: 36</i>

🇬🇧 <b>low</b> - not measuring much from the base to the top. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Others have proposed that hiccups may be caused by <b>low</b> levels of CO2 in the first place, and therefore high levels would inhibit the hiccups."</i> <a href="https://www.bbc.com/future/article/20140127-do-hiccup-remedies-work">[135_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>низький</b> - який має малу відстань від нижньої частини до верхньої або який має висоту меншу від звичайної для таких предметів. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Інші припускають, що саме <b>низький</b> рівень СО2 і є причиною гикавки і тому збільшення його в крові зупиняє симптом."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/03/160329_vert_do_hiccup_remedies_work_vp">[135_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣4️⃣0️⃣ make / зробити":

    """
1️⃣4️⃣0️⃣

💫 <b>make / зробити</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 962 / частота: 258</i>

🇬🇧 <b>make</b> - to produce something, often using a particular substance or material. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"Alcohol itself contains calories, not to mention all the sugars that <b>make</b> our favourite drinks so tasty."</i> <a href="https://www.bbc.com/future/article/20151026-is-beer-better-or-worse-for-you-than-wine">[197_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>зробити</b> - виготовити який-небудь предмет, якусь річ. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Алкоголь і сам по собі містить калорії, не кажучи вже про цукор, який додають в наші улюблені напої, щоби <b>зробити</b> їх ще смачнішими."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/11/151106_vert_fut_is_beer_better_or_worse_for_you_than_wine_vp">[197_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣4️⃣1️⃣ man / чоловік":

    """
1️⃣4️⃣1️⃣

💫 <b>man / чоловік</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 299 / частота: 256</i>

🇬🇧 <b>man</b> - an adult male human being. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"I’m a crier. I’m not ashamed. I’m a <b>man</b> who cries. Not in real life of course, but when watching movies."</i> <a href="https://www.bbc.com/future/article/20160529-everything-you-need-to-know-about-crying">[169_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>чоловік</b> - особа чоловічої статі. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Я часто плачу. І мені не соромно. Я <b>чоловік</b>, який плаче. Не в реальному житті, звичайно, але коли дивлюсь фільми."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/06/160531_vert_fut_everything_you_need_to_know_about_crying_vp">[169_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣4️⃣2️⃣ mean / означати": 
    
    """
1️⃣4️⃣2️⃣

💫 <b>mean / означати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 333 / частота: 159</i>

🇬🇧 <b>mean</b> - to express or represent something such as an idea, thought, or fact. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Osaka is known for being business-focussed, which <b>means</b> that people work and commute late into the night.</i> <a href="https://www.bbc.com/travel/article/20150529-living-in-the-worlds-safest-cities">[68_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>означати</b> - мати певне значення, певний зміст. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Життя в Осаці зосереджене на бізнесі. Це <b>означає</b>, що людям доводиться працювати й користуватися громадським транспортом до глибокої ночі.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-40521665">[68_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣4️⃣3️⃣ measure / вимірювати": 
    
    """
1️⃣4️⃣3️⃣

💫 <b>measure / вимірювати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 96 / частота: 8</i>

🇬🇧 <b>measure</b> - to discover the exact size or amount of something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“The smarter we are – as <b>measured</b> by how carefully we solve puzzles and how good we are at numbers – the better we are at twisting the facts around to make us feel the way we want to feel,” says Ropeik.</i> <a href="https://www.bbc.com/future/article/20160225-chemonoia-the-fear-blinding-our-minds-to-real-dangers">[158_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>вимірювати</b> - визначати величину чого-небудь, міряючи, порівнюючи її з одиницею виміру, застосовуючи спеціальні прилади або якусь мірку. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Що розумнішими ми стаємо (якщо <b>вимірювати</b> інтелект вмінням розв'язувати головоломки та здатністю до арифметики), то ефективніше маніпулюємо фактами, щоб відчувати себе так, як нам хотілося би," – відзначає Ропейк.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/04/160413_vert_fut_chemonoia_the_fear_blinding_our_minds_to_real_dangers_vp">[158_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣4️⃣4️⃣ meet / зустрічати": 
    
    """
1️⃣4️⃣4️⃣

💫 <b>meet / зустрічати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 133 / частота: 23</i>

🇬🇧 <b>meet</b> - to see and talk to someone for the first time. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>If you <b>meet</b> someone that looks like you, you have an instant bond because you share something.</i> <a href="https://www.bbc.com/future/article/20160712-you-are-surprisingly-likely-to-have-a-living-doppelganger">[172_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>зустрічати</b> - натрапляти на кого-, що-небудь на своєму шляху, десь, в якомусь місці. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Коли <b>зустрічаєш</b> людину, схожу на себе, відчуваєш миттєвий зв'язок з нею, адже ви маєте дещо спільне.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/07/160719_vert_fut_you_may_have_a_living_doppelganger_vp">[172_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣4️⃣5️⃣ memory / пам'ять": 
    
    """
1️⃣4️⃣5️⃣

💫 <b>memory / пам'ять</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 252 / частота: 245</i>

🇬🇧 <b>memory</b> - the ability to remember information, experiences, and people. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Numerous studies have shown that being multilingual can improve attention and <b>memory</b>.</i> <a href="https://www.bbc.com/future/article/20150528-how-to-learn-30-languages">[41_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>пам'ять</b> - здатність запам'ятовувати, зберігати і відтворювати в свідомості минулі враження. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Дослідження показують, що багатомовність поліпшує увагу та <b>пам'ять</b>.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150804_vert_fut_how_to_learn_30_languages_vp">[41_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣4️⃣6️⃣ million / мільйон": 
    
    """
1️⃣4️⃣6️⃣

💫 <b>million / мільйон</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 119 / частота: 98</i>

🇬🇧 <b>million</b> - the number 1,000,000. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“For a large chain that might have a <b>million</b> people a day coming into their restaurants around the world, it can take up to 18 months to put out a menu as we test everything on it three times,” says Gregg Rapp, a menu engineer based in Palm Springs, California.</i> <a href="https://www.bbc.com/future/article/20171120-the-secret-tricks-hidden-inside-restaurant-menus">[103_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>мільйон</b> - назва числа 1 000 000 і його цифрового позначення. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"У великих мережах, які щодня відвідує близько <b>мільйона</b> людей, складання меню може зайняти до півтора року, оскільки ми тричі тестуємо його", - каже Ґрегг Репп, інженер меню із міста Палм-Спрінгс у Каліфорнії.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-42100075">[103_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣4️⃣7️⃣ mind / розум": 
    
    """
1️⃣4️⃣7️⃣

💫 <b>mind / розум</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 226 / частота: 95</i>

🇬🇧 <b>mind</b> - the part of a person that makes it possible for him or her to think, feel emotions, and understand things. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Humans have been collecting records of dreams for years. But what do these archives of our nightly visions tell us about the human <b>mind</b>?</i> <a href="https://www.bbc.com/future/article/20160727-what-we-learnt-from-reading-peoples-dreams">[190_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>розум</b> - здатність людини мислити, відображати і пізнавати об'єктивну дійсність. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>В одному експерименті американського вченого люди десятиліттями записували свої сни. Чи можуть ці архіви допомогти нам краще зрозуміти людський <b>розум</b>?</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/08/160830_vert_fut_what_we_learnt_from_reading_peoples_dreams_vp">[190_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣4️⃣8️⃣ minute / хвилина": 
    
    """
1️⃣4️⃣8️⃣

💫 <b>minute / хвилина</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 129 / частота: 105</i>

🇬🇧 <b>minute</b> - one of the 60 parts that an hour is divided into, consisting of 60 seconds. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>We agreed to meet the family at 4 pm, and set off to explore on our own. It took us 20 <b>minutes</b> to circle the island, another 10 to walk across the interior’s main path.</i> <a href="https://www.bbc.com/travel/article/20160412-where-marrying-a-local-is-forbidden">[43_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>хвилина</b> - одиниця виміру часу, що дорівнює 1/60 години, або 60 секундам. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Ми домовилися зустрітися з родиною о четвертій і вирушили досліджувати острів самостійно. Ми обійшли його всього за 20 <b>хвилин</b>, а ще за 10 – прогулялися головною доріжкою всередині острова.</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/04/160422_vert_tra_where_marrying_a_local_is_forbidden_vp">[43_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣4️⃣9️⃣ money / гроші": 
    
    """
1️⃣4️⃣9️⃣

💫 <b>money / гроші</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 110 / частота: 92</i>

🇬🇧 <b>money</b> - coins or notes (= special pieces of paper) that are used to buy things, or an amount of these that a person has. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“I’m interested in human intuition and economic irrationalities,” he says. “There’s this sort of irrational feeling that if <b>money</b> is physical, it’s more yours, and you feel like you own it more. If you touch a dollar more, then that particular dollar becomes yours.”</i> <a href="https://www.bbc.com/future/article/20150724-the-truth-about-the-death-of-cash">[98_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>гроші</b> - металеві і паперові знаки, що є мірою вартості при купівлі і продажу. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Мене цікавить людська інтуїція і економічна ірраціональність, – каже він. – Нам властиве ірраціональне відчуття, нібито фізичні <b>гроші</b> більшою мірою нам належать. Чим довше ви тримаєте в руках доларову купюру, тим більше вона стає вашою".</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/09/160909_vert_fut_truth_about_the_death_of_cash_vp">[98_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣5️⃣0️⃣ month / місяць": 
    
    """
1️⃣5️⃣0️⃣

💫 <b>month / місяць</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 108 / частота: 97</i>

🇬🇧 <b>month</b> - a period of about four weeks, especially one of the twelve periods into which a year is divided. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“I lived in a master plan community that had a golf course, man-made beach, indoor/outdoor tennis,” Musgrove said. “My house was also pretty big with a private swimming pool for $1,300 a <b>month</b>.”</i> <a href="https://www.bbc.com/travel/article/20170917-the-surprising-side-to-las-vegas-that-few-know">[12_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>місяць</b> - проміжок часу, протягом якого це небесне тіло обертається навколо Землі (від 28 до 31 доби). <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Я жив у районі, у якому було поле для гольфу, штучний пляж, відкритий і закритий тенісний корт, - розповідає Масгроув. - У мене був досить великий будинок із власним басейном, який коштував лише 1300 дол. на <b>місяць</b>".</i> <a href="https://www.bbc.com/ukrainian/vert-tra-44266837">[12_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣5️⃣1️⃣ move / рухатися": 
    
    """
1️⃣5️⃣1️⃣

💫 <b>move / рухатися</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 149 / частота: 35</i>

🇬🇧 <b>move</b> - to (cause to) change position. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>A series of investigations by psychologist Constantine Sedikides suggest nostalgia may act as a resource that we can draw on to connect to other people and events, so that we can <b>move</b> forward with less fear and greater purpose.</i> <a href="https://www.bbc.com/future/article/20140603-why-nostalgia-is-good-for-you">[149_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>рухатися</b> - переміщатися, пересуватися. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Низка досліджень, проведених психологом Костянтином Седікідесом, показала, що ностальгія допомагає нам відчувати зв'язок з іншими людьми і подіями, завдяки чому ми можемо сміливіше <b>рухатися</b> вперед та краще усвідомлювати свої цілі.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/02/160217_vert_fut_why_nostalgia_is_good_for_you_vp">[149_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣5️⃣2️⃣ name / ім'я": 
    
    """
1️⃣5️⃣2️⃣

💫 <b>name / ім'я</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 244 / частота: 211</i>

🇬🇧 <b>name</b> - the word or words that a person, thing, or place is known by. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Does our <b>name</b> decide our fate? While we may brush these cases aside as coincidence, some surprising new studies would suggest that in some small way, it does.</i> <a href="https://www.bbc.com/future/article/20161102-your-name-reveals-more-than-you-think">[171_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>ім'я</b> - особиста назва людини, що дається їй після народження. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Чи визначає <b>ім'я</b> нашу долю? Хоча ми можемо легко відкинути ці приклади як простий збіг обставин, останні дослідження припускають, що певним чином це можливо.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/11/161103_vert_fut_your_name_reveals_a_lot_vp">[171_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣5️⃣3️⃣ need / потребувати": 
    
    """
1️⃣5️⃣3️⃣

💫 <b>need / потребувати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 311 / частота: 40</i>

🇬🇧 <b>need</b> - to have to have something, or to want something very much. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Up to 45% of teenagers bite their nails, for example; teenagers may be a handful but you wouldn't argue that nearly half of them <b>need</b> medical intervention.</i> <a href="https://www.bbc.com/future/article/20140710-why-do-we-bite-our-nails">[63_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>потребувати</b> - відчувати нестачу чогось, необхідність у кому-, чому-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>45% підлітків гризуть нігті, але ви ж не станете стверджувати, що майже половина з них <b>потребує</b> медичної допомоги.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150817_vert_fut_why_do_we_bite_nails_vp">[63_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣5️⃣4️⃣ never / ніколи": 
    
    """
1️⃣5️⃣4️⃣

💫 <b>never / ніколи</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 163 / частота: 107</i>

🇬🇧 <b>never</b> - not at any time or not on any occasion. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>It is <b>never</b> too late to learn another tongue, and it can be very rewarding. Alex Rawlings is a British professional polyglot who speaks 15 languages: “Each language gives you a whole new lifestyle, a whole new shade of meaning,” he says. “It’s addictive!”</i> <a href="https://www.bbc.com/future/article/20160811-the-amazing-benefits-of-being-bilingual">[27_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>ніколи</b> - ні в який час, ні за яких обставин. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Вивчати іншу мову <b>ніколи</b> не буває надто пізно. Професійний поліглот, британець Алекс Ролінгс, який розмовляє 15 мовами, каже, що "кожна мова дає вам абсолютно новий спосіб життя, нові відтінки значення. Це викликає залежність!"
</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/08/160816_vert_fut_amazing_benefits_of_being_bilingual_vp">[27_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣5️⃣5️⃣ new / новий": 
    
    """
1️⃣5️⃣5️⃣

💫 <b>new / новий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 400 / частота: 297</i>

🇬🇧 <b>new</b> - recently created or having started to exist recently. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>In 1958, China’s ruling party announced an ambitious <b>new</b> project: the Great Leap Forward, which they hoped would propel the nation of peasant farmers to industrial glory in the space of a few years.</i> <a href="https://www.bbc.com/future/article/20161014-why-billionaires-have-more-sons">[170_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>новий</b> - який недавно виник, з'явився, не існував раніше; недавно зроблений, створений і т. ін. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>У 1958 році уряд Китаю оголосив <b>новий</b> амбітний проект – "Великий стрибок", який мав на меті за кілька років перетворити націю селян на індустріальну країну.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/10/161017_vert_fut_why_billionaires_have_more_sons_vp">[170_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣5️⃣6️⃣ next / наступний": 
    
    """
1️⃣5️⃣6️⃣

💫 <b>next / наступний</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 134 / частота: 124</i>

🇬🇧 <b>next</b> - being the first one after the present one or after the one just mentioned. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>My Balkan road trip was taking me out of Croatia, and I wasn’t even entirely sure that my <b>next</b> destination existed.</i> <a href="https://www.bbc.com/travel/article/20160219-cheese-beer-and-a-wonderful-view">[37_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>наступний</b> - який наступає, розташовується або з'являється слідом за ким-, чим-небудь; найближчий після когось, чогось. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Мій шлях Балканським півостровом пролягав за межі Хорватії, але що чекало мене попереду і чи існував взагалі мій <b>наступний</b> пункт призначення, я точно не знав.</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/02/160225_vert_tra_cheese_beer_and_a_wonderful_view_vp">[37_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣5️⃣7️⃣ night / ніч": 
    
    """
1️⃣5️⃣7️⃣

💫 <b>night / ніч</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 120 / частота: 47</i>

🇬🇧 <b>night</b> - the part of every 24-hour period when it is dark because there is very little light from the sun. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>As you move to higher latitudes, the <b>night</b> can last up to 16 hours in the winter, so living in that kind of environment may have led Northern European ancestors to fragment their evening slumber during that part of the year.</i> <a href="https://www.bbc.com/future/article/20170220-the-surprising-truth-about-why-we-sleep-and-how-much-we-need">[179_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>ніч</b> - частина доби від заходу до сходу сонця, з вечора до ранку. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>В інших широтах <b>ніч</b> може тривати до 16 годин взимку, а отже, стародавні мешканці Північної Європи справді могли спати уривками упродовж довгих годин темряви.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-39131741">[179_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣5️⃣8️⃣ now / зараз": 
    
    """
1️⃣5️⃣8️⃣

💫 <b>now / зараз</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 309 / частота: 123</i>

🇬🇧 <b>now</b> - at the present time, not in the past or future. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>And you can <b>now</b> buy EEG kits that work with your smartphone, potentially opening the door for games that help you boost memory consolidation.</i> <a href="https://www.bbc.com/future/article/20140721-how-to-learn-while-you-sleep">[28_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>зараз</b> - у даний час, тепер. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i><b>Зараз</b> вже можна купити прилади для електроенцефалографії (ЕЕГ), які поєднуються зі смартфоном і це відкриває перспективи для створення ігор, корисних для стимуляції пам'яті.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/05/160530_vert_fut_how_to_learn_while_you_sleep_vp">[28_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣5️⃣9️⃣ number / число": 
    
    """
1️⃣5️⃣9️⃣

💫 <b>number / число</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 199 / частота: 70</i>

🇬🇧 <b>number</b> - (a sign or symbol representing) a unit that forms part of the system of counting and calculating. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>The <b>number</b> pi, which is celebrated with its own day on 14 March, has inspired “Pilish” – a fiendishly challenging form of writing. There’s even a Pilish novel.</i> <a href="https://www.bbc.com/future/article/20160311-how-the-number-pi-inspired-a-writing-style">[152_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>число</b> - поняття, за допомогою якого передається кількість і провадиться лічба. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i><b>Число</b> пі, день якого неофіційно відзначають 14 березня (в американському форматі дати – 3.14), надихнуло на створення мови пі, якою написані поеми і навіть один роман.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/03/160314_vert_fut_how_the_number_pi_inspired_a_writing_style_vp">[152_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣6️⃣0️⃣ offer / запропонувати": 
    
    """
1️⃣6️⃣0️⃣

💫 <b>offer / запропонувати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 101 / частота: 52</i>

🇬🇧 <b>offer</b> - to ask someone if they would like to have something or if they would like you to do something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>But in the northern hemisphere at least, these findings could <b>offer</b> a simple way to kill the germs while they are still hanging in the air.</i> <a href="https://www.bbc.com/future/article/20151016-the-real-reason-germs-spread-in-the-winter">[140_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>запропонувати</b> - виявити бажання, готовність допомогти кому-небудь або віддати кого-, що-небудь у чиєсь розпорядження. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Втім, у північній півкулі, де віруси протягом деякого часу залишаються в повітрі, можна <b>запропонувати</b> простий спосіб позбутися їх.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151023_vert_fut_reason_flu_spreads_in_the_winter_vp">[140_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣6️⃣1️⃣ often / часто": 
    
    """
1️⃣6️⃣1️⃣

💫 <b>often / часто</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 304 / частота: 216</i>

🇬🇧 <b>often</b> - many times. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>We <b>often</b> find ourselves laughing at the strangest of moments. As psychologists are discovering, those helpless giggles might be one of our most important and profound behaviours.</i> <a href="https://www.bbc.com/future/article/20150320-why-do-we-laugh-inappropriately">[187_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>часто</b> - коли щось відбувається, надходить, з'являється, трапляється і т. ін. через короткі проміжки часу. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i><b>Часто</b> ми не можемо втриматися від сміху у найбільш невчасний момент. Утім, психологи кажуть, що цей недоречний регіт є найважливішою та найглибшою рисою підсвідомості людини.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150925_vert_fut_why_do_we_laugh_inappropriately_vp">[187_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣6️⃣2️⃣ old / старий": 
    
    """
1️⃣6️⃣2️⃣

💫 <b>old / старий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 239 / частота: 60</i>

🇬🇧 <b>old</b> - having lived or existed for many years. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>It has an <b>old</b> quarter with a well-preserved Plaza Mayor and churches that date back to medieval times.</i> <a href="https://www.bbc.com/travel/article/20170615-the-town-that-split-the-world-in-two">[11_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>старий</b> - який існує довгий час, давно створений. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i><b>Старий</b> центр міста з головною площею Пласа-Майор і середньовічними церквами добре зберігся.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-43729118">[11_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣6️⃣3️⃣ once / колись": 
    
    """
1️⃣6️⃣3️⃣

💫 <b>once / колись</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 167 / частота: 57</i>

🇬🇧 <b>once</b> - one single time. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Food was <b>once</b> seen as a source of sustenance and pleasure. Today, the dinner table can instead begin to feel like a minefield.</i> <a href="https://www.bbc.com/future/article/20151029-are-any-foods-safe-to-eat-anymore-heres-the-truth">[108_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>колись</b> - у якийсь час, у минулому. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i><b>Колись</b> давно їжа була джерелом енергії та задоволення. Сьогодні обідній стіл перетворився на справжнє мінне поле.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151215_vert_fut_are_any_foods_safe_to_eat_anymore_heres_the_truth_vp">[108_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣6️⃣4️⃣ only / лише": 
    
    """
1️⃣6️⃣4️⃣

💫 <b>only / лише</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 496 / частота: 476</i>

🇬🇧 <b>only</b> - used to show that there is a single one or very few of something, or that there are no others. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>In any case, a modern city is a grossly artificial bubble, supported <b>only</b> by the civilisation that constructed it.</i> <a href="https://www.bbc.com/future/article/20161124-how-to-cope-with-the-end-of-the-world">[26_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>лише</b> - уживається для виділення, обмеження у знач. тільки, виключно. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Сучасне місто - це штучна система, комфорт якої можливий <b>лише</b> за постійної підтримки цивілізації.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-38184129">[26_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣6️⃣5️⃣ pain / біль": 
    
    """
1️⃣6️⃣5️⃣

💫 <b>pain / біль</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 101 / частота: 92</i>

🇬🇧 <b>pain</b> - a feeling of physical suffering caused by injury or illness. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>If the same thing happened in a human this would press on the nerves, causing back <b>pain</b>, and possibly even a herniated disc.</i> <a href="https://www.bbc.com/future/article/20160418-the-surprising-downsides-of-sit-ups">[164_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>біль</b> - відчуття фізичного страждання. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Якщо в хребті людини відбуваються подібні процеси, диски можуть тиснути нерви, викликаючи <b>біль</b> у спині, і навіть, можливо, грижу міжхребцевого диска.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/04/160421_vert_fut_the_surprising_downsides_of_sit_ups_vp">[164_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣6️⃣6️⃣ part / частина": 
    
    """
1️⃣6️⃣6️⃣

💫 <b>part / частина</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 295 / частота: 211</i>

🇬🇧 <b>part</b> - some but not all of a thing. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>This sense is known as proprioception and it’s the awareness we have of where each of our body <b>parts</b> is located in space.</i> <a href="https://www.bbc.com/future/article/20141118-how-many-senses-do-you-have">[61_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>частина</b> - окрема одиниця, пайка, шматок і т. ін., які відділяються від чогось цілого. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Це чуття називається пропріорецепція, тобто усвідомлення, де перебуває кожна <b>частина</b> нашого тіла.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150917_vert_fut_how_many_senses_do_you_have_vp">[61_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣6️⃣7️⃣ participant / учасник": 
    
    """
1️⃣6️⃣7️⃣

💫 <b>participant / учасник</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 115 / частота: 274</i>

🇬🇧 <b>participant</b> - a person who takes part in or becomes involved in a particular activity. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Before they went in the scanner each <b>participant</b> filled out a personality profile and contributed a mouth swab for genetic analysis.</i> <a href="https://www.bbc.com/future/article/20130717-what-makes-someone-an-extrovert">[185_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>учасник</b> - той, хто бере або брав участь у чому-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Перед скануванням кожен <b>учасник</b> заповнив анкету, яка визначала тип його особистості, і здав мазок з ротової порожнини для генетичного аналізу.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/02/160204_vert_fut_what_makes_someone_an_extrovert_vp">[185_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣6️⃣8️⃣ person / людина": 
    
    """
1️⃣6️⃣8️⃣

💫 <b>person / людина</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 1596 / частота: 903</i>

🇬🇧 <b>person</b> - a man, woman, or child. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Your genes, your friends, the schools you attended, plus many other factors, will all have played a part in making you the <b>person</b> you are today.</i> <a href="https://www.bbc.com/future/article/20160907-clues-to-your-personality-appeared-before-you-could-talk">[144_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>людина</b> - будь-яка особа; кожний. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Генетична спадковість, друзі, школа, в якій ви вчились, та багато інших факторів зіграли свою роль в становленні тієї <b>людини</b>, якою ви є сьогодні.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/09/160909_vert_fut_personality_child_vp">[144_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣6️⃣9️⃣ personality / особистість": 
    
    """
1️⃣6️⃣9️⃣

💫 <b>personality / особистість</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 206 / частота: 151</i>

🇬🇧 <b>personality</b> - the type of person you are, shown by the way you behave, feel, and think. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>This idea that you gain a new <b>personality</b> with every language you speak, that you act differently when speaking different languages, is a profound one.</i> <a href="https://www.bbc.com/future/article/20160811-the-amazing-benefits-of-being-bilingual">[27_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>особистість</b> - конкретна людина з погляду її культури, особливостей характеру, поведінки і т. ін. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Думка, що з кожною мовою ви отримуєте нову <b>особистість</b> і що, мова, якою ви користуєтесь, впливатиме не лише на ваш хід думок, але й поведінку, стара як світ.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/08/160816_vert_fut_amazing_benefits_of_being_bilingual_vp">[27_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣7️⃣0️⃣ place / місце": 
    
    """
1️⃣7️⃣0️⃣

💫 <b>place / місце</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 257 / частота: 254</i>

🇬🇧 <b>place</b> - an area, town, building, etc. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“It is a unique <b>place</b> in our planet. It truly is.” “It should be preserved as a World Heritage site.”</i> <a href="https://www.bbc.com/travel/article/20181111-the-buried-secrets-of-the-deadliest-location-on-earth">[32_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>місце</b> - простір земної поверхні, зайнятий або який може бути зайнятий ким-, чим-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Це унікальне <b>місце</b> на нашій планеті. Його слід берегти як об'єкт світової спадщини", - підсумовує науковець.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-46323405">[32_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣7️⃣1️⃣ play / грати": 
    
    """
1️⃣7️⃣1️⃣

💫 <b>play / грати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 124 / частота: 37</i>

🇬🇧 <b>play</b> - when you play, especially as a child, you spend time doing an enjoyable and/or entertaining activity. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“If the clothes were blue they assumed it was a boy, <b>played</b> more physical games with them and encouraged them to play with a squeaky hammer.”</i> <a href="https://www.bbc.com/future/article/20141117-the-pink-vs-blue-gender-myth">[188_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>грати</b> - проводити час, забавляючись, розважаючись. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Якщо одяг на дитині був блакитний, учасниці експерименту вважали, що це хлопчик, і починали <b>грати</b> з ним у більш енергійні ігри та пропонували дитині молоточок з пискавкою."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151229_vert_fut_the_pink_vs_blue_gender_myth_vp">[188_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣7️⃣2️⃣ point / точка": 
    
    """
1️⃣7️⃣2️⃣

💫 <b>point / точка</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 201 / частота: 61</i>

🇬🇧 <b>point</b> - a particular time or stage reached in a process. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“The highest <b>point</b> on the entire island is only 6m high – a man-made mound called ‘Refuge Hill’ where the residents cluster during summer cyclones.”</i> <a href="https://www.bbc.com/travel/article/20160412-where-marrying-a-local-is-forbidden">[43_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>точка</b> - певне місце, пункт у просторі, на місцевості, у середині або на поверхні чогось. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Найвища <b>точка</b> острова здіймається всього на 6 метрів у висоту – це штучний курган під назвою 'Притулок Гілл', де жителі ховаються під час літніх циклонів."</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2016/04/160422_vert_tra_where_marrying_a_local_is_forbidden_vp">[43_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣7️⃣3️⃣ possible / можливий": 
    
    """
1️⃣7️⃣3️⃣

💫 <b>possible / можливий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 131 / частота: 59</i>

🇬🇧 <b>possible</b> - able to be done or achieved, or able to exist. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Proprioception is <b>possible</b> thanks to receptors in our muscles known as spindles, which tell the brain about the current length and stretch of the muscles.”</i> <a href="https://www.bbc.com/future/article/20141118-how-many-senses-do-you-have">[61_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>можливий</b> - який можна здійснити, виконати. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Пропріорецепція <b>можлива</b> завдяки особливим рецепторам м'язів, які повідомляють мозок про поточну довжину і напругу м'язів."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150917_vert_fut_how_many_senses_do_you_have_vp">[61_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣7️⃣4️⃣ probably / ймовірно": 
    
    """
1️⃣7️⃣4️⃣

💫 <b>probably / ймовірно</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 120 / частота: 18</i>

🇬🇧 <b>probably</b> - used to mean that something is very likely. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“For a start, they are in such a deep sleep that they will <b>probably</b> not notice you, even if you try to wake them.”</i> <a href="https://www.bbc.com/future/article/20120208-it-is-dangerous-to-wake-a-sleepwa">[156_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>ймовірно</b> - те, що можна здійснити, виконати. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Почнемо з того, що сновида спить так глибоко, що, <b>ймовірно</b>, і зовсім не помітить вас, навіть якщо ви спробуєте його розбудити."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-45446558">[156_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣7️⃣5️⃣ problem / проблема": 
    
    """
1️⃣7️⃣5️⃣

💫 <b>problem / проблема</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 153 / частота: 173</i>

🇬🇧 <b>problem</b> - a situation, person, or thing that needs attention and needs to be dealt with or solved. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Humans would be in deep trouble if they had to fight intelligent bacteria, especially the really bad ones,” Call says. “The <b>problem</b> is we could not get rid of them all, because they are essential for our own survival.”</i> <a href="https://www.bbc.com/future/article/20160824-what-would-happen-if-all-animals-were-as-smart-as-us">[198_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>проблема</b> - складне теоретичне або практичне питання, що потребує вирішення. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>“Люди опинились би у великій халепі, якби їм довелось протистояти розумним бактеріям, особливо поганим,” – зазначає Хосеп Колл. “<b>Проблема</b> в тому, що ми не зможемо знищити їх усіх, оскільки вони необхідні для нашого виживання.”</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/08/160826_vert_fut_if_all_animals_were_as_smart_as_us_vp">[198_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣7️⃣6️⃣ produce / виробляти":

    """
1️⃣7️⃣6️⃣

💫 <b>produce / виробляти</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 109 / частота: 54</i>

🇬🇧 <b>produce</b> - to make something or bring something into existence. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Having grown up on a farm in Northern Ireland’s County Antrim, Elliott has a sound understanding of how to <b>produce</b> quality food.”</i> <a href="https://www.bbc.com/future/article/20160726-toxins-uncovered-at-a-food-fraud-lab">[137_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>виробляти</b> - виготовляти що-небудь, робити якісь речі, предмети і т. ін. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>“Кріс Елліот виріс на фермі у графстві Антрім на півночі Ірландії, і він чудово розуміє, як <b>виробляти</b> якісну їжу.”</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/08/160802_vert_fut_toxins_uncovered_at_a_food_fraud_lab_vp">[137_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣7️⃣7️⃣ psychologist / психолог": 
    
    """
1️⃣7️⃣7️⃣

💫 <b>psychologist / психолог</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 155 / частота: 155</i>

🇬🇧 <b>psychologist</b> - someone who studies the human mind and human emotions and behavior, and how different situations have an effect on people. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“The cheeks will be raised but we pull the corners of the mouth downwards or press the lips together, like ‘I shouldn’t be smiling’,” says Zara Ambadar, a cognitive <b>psychologist</b> at the University of Pittsburgh.</i> <a href="https://www.bbc.com/future/article/20170407-why-all-smiles-are-not-the-same">[199_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>психолог</b> - фахівець з психології. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>“Стримуючи усмішку, ми опускаємо куточки рота вниз або стискаємо губи, ніби говорячи, 'я не маю усміхатися'”, – пояснює Зара Амбадар, когнітивний <b>психолог</b> з Університету Піттсбурга.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-39568520">[199_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣7️⃣8️⃣ public / публічний": 
    
    """
1️⃣7️⃣8️⃣

💫 <b>public / публічний</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 113 / частота: 7</i>

🇬🇧 <b>public</b> - relating to or involving people in general, rather than being limited to a particular group of people. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“In fact, there is some evidence that tea can soothe your nerves: regular tea drinkers do tend to show a calmer physiological response to unsettling situations (such as <b>public</b> speaking).”</i> <a href="https://www.bbc.com/future/article/20160115-tea-vs-coffee-which-drink-is-better-for-you">[16_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>публічний</b> - який відбувається в присутності публіки, людей. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Деякі дані дійсно підтверджують, що чай справляє заспокійливий ефект на нерви, а затяті прихильники чаю, як правило, стійкіше реагують на стресові ситуації, як-от <b>публічний</b> виступ."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-41500645">[16_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣7️⃣9️⃣ put / класти":

    """
1️⃣7️⃣9️⃣

💫 <b>put / класти</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 165 / частота: 8</i>

🇬🇧 <b>put</b> - to move something or someone into the stated place, position, or direction. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“It’s a window into how we manage to coordinate complex actions, matching plans with actions in a way that – most of the time – allows us to <b>put</b> the right bricks in the right place to build the cathedral of our lives.”</i> <a href="https://www.bbc.com/future/article/20160307-why-does-walking-through-doorways-make-us-forget">[123_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>класти</b> - поміщати в що-, куди-небудь; розміщувати десь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Отже, ця особливість нашого розуму допомагає зрозуміти, як нам вдається координувати складні дії та планувати їх відповідно більш загальної мети. Іншими словами, як нам вдається <b>класти</b> цеглину за цеглиною в правильному порядку, будуючи складний собор нашого життя."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/03/160310_vert_fut_why_does_walking_through_doorways_make_us_forget_vp">[123_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣8️⃣0️⃣ question / питання":

    """
1️⃣8️⃣0️⃣

💫 <b>question / питання</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 192 / частота: 231</i>

🇬🇧 <b>question</b> - a sentence or phrase used to find out information. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Many scientists believe the cause to simply be radio interference. However, the episode has raised the <b>question</b> of how we are able to distinguish one space sound from another in our search for a sign of life.”</i> <a href="https://www.bbc.com/future/article/20160223-what-would-happen-if-aliens-contacted-earth">[118_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>питання</b> - Звертання до кого-небудь, яке потребує відповіді, роз'яснення і т. ін. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Багато вчених упевнені, що це були звичайні радіоперешкоди. Однак той випадок поставив важливе <b>питання</b>: як відрізнити космічний шум від навмисної радіопередачі?"</i> <a href="https://www.bbc.com/ukrainian/vert-fut-42011509">[118_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣8️⃣1️⃣ read / читати":

    """
1️⃣8️⃣1️⃣

💫 <b>read / читати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 176 / частота: 45</i>

🇬🇧 <b>read</b> - to look at words or symbols and understand what they mean. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“If you wiggle your head around while <b>reading</b>, for example, you’ll see that it makes little difference to your ability to read and stay focused on the words.”</i> <a href="https://www.bbc.com/future/article/20141118-how-many-senses-do-you-have">[61_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>читати</b> - сприймати що-небудь записане літерами, письмовими знаками і т. ін. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Якщо ви легко похитаєте головою під час <b>читання</b>, то помітите, що ці рухи майже не впливають на вашу здатність читати і зосереджуватися на словах."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150917_vert_fut_how_many_senses_do_you_have_vp">[61_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣8️⃣2️⃣ real / реальний":

    """
1️⃣8️⃣2️⃣

💫 <b>real / реальний</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 129 / частота: 56</i>

🇬🇧 <b>real</b> - existing in fact and not imaginary. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“The problem is that people in a clinical trial are given exactly the same health warnings whether they are taking the <b>real</b> drug or the placebo.”</i> <a href="https://www.bbc.com/future/article/20150210-can-you-think-yourself-to-death">[47_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>реальний</b> - який існує в об'єктивній дійсності; дійсний. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Річ у тім, що пацієнти під час клінічних тестів отримують однакові попередження про можливі побічні ефекти - незалежно від того, отримують вони <b>реальний</b> препарат чи плацебо."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150707_vert_fut_killing_thoughts_vp">[47_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣8️⃣3️⃣ really / справді":

    """
1️⃣8️⃣3️⃣

💫 <b>really / справді</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 208 / частота: 79</i>

🇬🇧 <b>really</b> - in fact. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“But do the British <b>really</b> apologise more frequently than members of other cultures? If so, what’s the reason for this peculiar verbal tic… and how bad a habit is it?”</i> <a href="https://www.bbc.com/future/article/20160223-why-do-the-british-say-sorry-so-much">[66_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>справді</b> - у дійсності, насправді, дійсно. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Втім, хіба британці і <b>справді</b> вибачаються частіше, ніж представники інших культур? Якщо так, то в чому причина цього дивного словесного тику і наскільки поганою є ця звичка?"</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/03/160301_vert_fut_why_do_the_british_say_sorry_so_much_vp">[66_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣8️⃣4️⃣ reason / причина": 
    
    """
1️⃣8️⃣4️⃣

💫 <b>reason / причина</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 158 / частота: 162</i>

🇬🇧 <b>reason</b> - the cause of an event or situation or something that provides an excuse or explanation. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“The <b>reason</b> it’s a prime candidate for sleepiness is that it contains the substance L-tryptophan. But other foods have more.”</i> <a href="https://www.bbc.com/future/article/20161220-are-some-foods-more-sleep-inducing-than-others">[08_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>причина</b> - підстава, привід для яких-небудь дій, вчинків. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"<b>Причина</b> в тому, що м'ясо індички містить речовину L-триптофан. В деяких продуктах, однак, цієї амінокислоти може бути значно більше."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-38462176">[08_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣8️⃣5️⃣ red / червоний": 
    
    """
1️⃣8️⃣5️⃣

💫 <b>red / червоний</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 153 / частота: 134</i>

🇬🇧 <b>red</b> - of the colour of fresh blood. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“The idea that <b>red</b> wakes us up or blue calms us down is deeply engrained in Western culture - to the point that many consider it a fact.”</i> <a href="https://www.bbc.com/future/article/20150402-do-colours-really-change-our-mood">[107_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>червоний</b> - який має забарвлення одного з основних кольорів спектра, що йде перед оранжевим. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"У свідомості представників західної культури вкоренилася думка, що <b>червоний</b> збуджує відчуття, тоді як блакитний – заспокоює. Дехто навіть вважає це доведеним фактом. Але наскільки це насправді так?"</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/06/160621_vert_fut_do_colours_really_change_our_mood_vp">[107_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣8️⃣6️⃣ remember / пам'ятати": 
    
    """
1️⃣8️⃣6️⃣

💫 <b>remember / пам'ятати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 168 / частота: 102</i>

🇬🇧 <b>remember</b> - to be able to bring back a piece of information into your mind, or to keep a piece of information in your memory. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“I asked Sabrije what she <b>remembered</b> of Yugoslavia. ‘Life was so much better back then,’ she said.”</i> <a href="https://www.bbc.com/travel/article/20180425-im-from-a-country-that-no-longer-exists">[65_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>пам'ятати</b> - зберігати в пам'яті, не забувати. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Я запитала Сабріє, що вона <b>пам'ятає</b> про Югославію. ‘Життя тоді було набагато кращим,’ - сказала вона."</i> <a href="https://www.bbc.com/ukrainian/features-44100405">[65_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣8️⃣7️⃣ research / дослідження": 
    
    """
1️⃣8️⃣7️⃣

💫 <b>research / дослідження</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 257 / частота: 747</i>

🇬🇧 <b>research</b> - a detailed study of a subject, especially in order to discover (new) information or reach a (new) understanding. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“But the <b>research</b> relied on people’s own estimations of how long they crossed their legs for. As I write this, I’m sitting at my desk and happen to have my legs crossed, but I would have no idea how many hours a day I spend sitting in this way.”</i> <a href="https://www.bbc.com/future/article/20151013-is-crossing-your-legs-bad-for-you">[59_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>дослідження</b> - науковий розгляд з метою пізнання, вияснення чогось. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Втім, це <b>дослідження</b> спиралося на оцінку самих людей, як довго вони сиділи у такій позі. Зараз, коли я пишу цю статтю, я сиджу за столом і мої ноги схрещені, але я й гадки не маю, скільки часу щодня я проводжу в такій позі."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151015_vert_fut_is_crossing_your_legs_bad_for_you_vp">[59_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣8️⃣8️⃣ researcher / дослідник": 
    
    """
1️⃣8️⃣8️⃣

💫 <b>researcher / дослідник</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 228 / частота: 336</i>

🇬🇧 <b>researcher</b> - someone who studies a subject, especially in order to discover new information or reach a new understanding. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Different cultures have different attachments to their currencies,” says Nicolas Christin, a <b>researcher</b> at Carnegie Mellon University, “and as far as the US is concerned there’s a strong attachment.”</i> <a href="https://www.bbc.com/future/article/20150724-the-truth-about-the-death-of-cash">[98_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>дослідник</b> - той, хто займається науковими дослідженнями, вивченням, обслідуванням чого-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Різні народи різною мірою прив’язані до своєї валюти, – каже Ніколас Крістін, <b>дослідник</b> з Університету Карнегі-Меллона. – Щодо США, там цей зв'язок дуже міцний."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/09/160909_vert_fut_truth_about_the_death_of_cash_vp">[98_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣8️⃣9️⃣ room / кімната": 
    
    """
1️⃣8️⃣9️⃣

💫 <b>room / кімната</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 120 / частота: 55</i>

🇬🇧 <b>room</b> - a part of the inside of a building that is separated from other parts by walls, floor, and ceiling. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>For me, distilleries are near magical places, where alchemy meets science to create something far greater than the sum of its parts. They are also museums of smells, where each <b>room</b> has a beautiful and distinct scent.</i> <a href="https://www.bbc.com/travel/article/20150511-why-you-should-never-drink-whisky-on-the-rocks">[53_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>кімната</b> - відокремлена стінами або перегородками частина будинку, квартири для проживання в ній. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Винокурні для мене – це чарівні місця, де зустрічаються наука і алхімія, щоби створити дещо значно більше, ніж сума первісних інгредієнтів. Вони також є музеями ароматів, де кожна <b>кімната</b> має свій власний неповторний запах.</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2015/12/151225_vert_tra_why_you_should_never_drink_whisky_on_the_rocks_vp">[53_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣9️⃣0️⃣ same / однаковий": 
    
    """
1️⃣9️⃣0️⃣

💫 <b>same / однаковий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 306 / частота: 36</i>

🇬🇧 <b>same</b> - exactly like another or each other. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>One possibility is that we imagine the future by pulling apart our recollections and then piecing them together in a montage that might represent a new scenario. In this way, memory and foresight use the <b>same</b> “mental time travel” in the <b>same</b> areas of the brain.</i> <a href="https://www.bbc.com/future/article/20150225-secrets-of-alice-in-wonderland">[46_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>однаковий</b> - який нічим не відрізняється від інших у чому-небудь; такий самий. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Коли ми уявляємо собі майбутнє, то зазвичай розкладаємо наші спогади на частини, а потім монтуємо їх у новий сценарій. Пам'ять і передбачення використовують <b>однаковий</b> спосіб "подорожі в розумовому часі" в одній і тій же ділянці мозку.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150708_vert_fut_alice_in_wonderland_psychology_vp">[46_BBC_Future_Corpus_UKR]</a>
    """,

   "1️⃣9️⃣1️⃣ say / сказати": 
    
    """
1️⃣9️⃣1️⃣

💫 <b>say / сказати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 1678 / частота: 78</i>

🇬🇧 <b>say</b> - to pronounce words or sounds, to express a thought, opinion, or suggestion, or to state a fact or instruction. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>If you’re being honest you’ve seen better, but as your child waits for your reaction, what do you <b>say</b>?</i> <a href="https://www.bbc.com/future/article/20140204-is-it-right-to-praise-a-child">[184_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>сказати</b> - передати словами думки, почуття тощо; висловитися, повідомити усно що-небудь; промовити. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Чесно кажучи, ви бачили і кращі твори, але, дивлячись в очі дитині, яка чекає на вашу реакцію, що можна <b>сказати</b>?</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151008_vert_fut_is_it_right_to_praise_a_child_vp">[184_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣9️⃣2️⃣ school / школа": 
    
    """
1️⃣9️⃣2️⃣

💫 <b>school / школа</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 121 / частота: 71</i>

🇬🇧 <b>school</b> - a place where children go to be educated. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>The first book in Euskara wasn’t printed until 1545 in Bordeaux, France; the first Basque <b>school</b> opened in 1914 in San Sebastian (only 30 years before Basque schools were forced underground by Franco).</i> <a href="https://www.bbc.com/travel/article/20170719-the-mysterious-origins-of-europes-oldest-language">[28_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>школа</b> - навчальний заклад, який здійснює загальну освіту і виховання молодого покоління. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Перша книга баскською вийшла друком лише в 1545 році у французькому місті Бордо. Перша баскська <b>школа</b> відкрилася в 1914 році в Сан-Себастьяні в Іспанії (лише за 30 років до того, як баскську заборонили).</i> <a href="https://www.bbc.com/ukrainian/vert-tra-40729382">[28_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣9️⃣3️⃣ science / наука": 
    
    """
1️⃣9️⃣3️⃣

💫 <b>science / наука</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 106 / частота: 65</i>

🇬🇧 <b>science</b> - (knowledge from) the careful study of the structure and behaviour of the physical world, especially by watching, measuring, and doing experiments, and the development of theories to describe the results of these activities. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>For me, distilleries are near magical places, where alchemy meets <b>science</b> to create something far greater than the sum of its parts.</i> <a href="https://www.bbc.com/travel/article/20150511-why-you-should-never-drink-whisky-on-the-rocks">[53_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>наука</b> - одна з форм суспільної свідомості, що дає об'єктивне відображення світу; система знань про закономірності розвитку природи і суспільства та способи впливу на оточуючий світ. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Винокурні для мене – це чарівні місця, де зустрічаються <b>наука</b> і алхімія, щоби створити дещо значно більше, ніж сума первісних інгредієнтів.</i> <a href="https://www.bbc.com/ukrainian/vert_tra/2015/12/151225_vert_tra_why_you_should_never_drink_whisky_on_the_rocks_vp">[53_BBC_Travel_Corpus_UKR]</a>
    """,

    "1️⃣9️⃣4️⃣ scientist / науковець": 
    
    """
1️⃣9️⃣4️⃣

💫 <b>scientist / науковець</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 123 / частота: 125</i>

🇬🇧 <b>scientist</b> - an expert who studies or works in one of the sciences. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Why are some people extraordinarily selfish, manipulative, and unkind? David Robson asks the <b>scientist</b> delving into the darkest sides of the human mind.</i> <a href="https://www.bbc.com/future/article/20150130-the-man-who-studies-evil">[54_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>науковець</b> - той, хто займається розробкою питань науки. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Чому деякі люди надзвичайно егоїстичні, деспотичні та недоброзичливі? Кореспондент BBC Future розмовляє із <b>науковцем</b>, який вивчає найтемніші сторони людського розуму.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150811_the_man_who_studies_evil_vp">[54_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣9️⃣5️⃣ see / бачити": 
    
    """
1️⃣9️⃣5️⃣

💫 <b>see / бачити</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 460 / частота: 127</i>

🇬🇧 <b>see</b> - to be conscious of what is around you by using your eyes. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“The idea was that if you wear glasses to allow you to <b>see</b> clearly in the distance, your eyeball tries to elongate itself when you focus on a close object in order to see it properly.”</i> <a href="https://www.bbc.com/future/article/20140513-do-glasses-weaken-your-eyesight">[182_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>бачити</b> - мати здатність сприймати зором. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Ідея полягала в тому, що якщо носити окуляри, які дозволяють чітко <b>бачити</b> на відстані, то, фокусуючись на близьких об'єктах, очне яблуко намагатиметься витягуватися, а це погіршує міопію."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/06/160624_vert_fut_do_spectacles_worsen_sight_vp">[182_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣9️⃣6️⃣ seem / здаватися": 
    
    """
1️⃣9️⃣6️⃣

💫 <b>seem / здаватися</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 371 / частота: 62</i>

🇬🇧 <b>seem</b> - to give the effect of being; to be judged to be. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Would one creature come to rule all others, much as we humans have done, or would our varied kind arrive at some sort of peaceful, enlightened coexistence? It might <b>seem</b> like an absurd thought experiment – it’s certainly not possible.”</i> <a href="https://www.bbc.com/future/article/20160824-what-would-happen-if-all-animals-were-as-smart-as-us">[198_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>здаватися</b> - мати в чиїйсь уяві той чи інший вигляд, набирати певних рис, властивостей, справляти на кого-небудь якесь враження. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Чи стане один вид керувати всіма іншими, як це зробили ми, люди, або всі живі істоти прийдуть до цивілізованого і мирного співіснування? Ідея <b>здається</b> на перший погляд абсурдною – цього, звичайно, ніколи не станеться."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/08/160826_vert_fut_if_all_animals_were_as_smart_as_us_vp">[198_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣9️⃣7️⃣ sense / сенс":

    """
1️⃣9️⃣7️⃣

💫 <b>sense / сенс</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 191 / частота: 46</i>

🇬🇧 <b>sense</b> - an ability to understand, recognize, value, or react to something, especially any of the five physical abilities to see, hear, smell, taste, and feel. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“From an evolutionary standpoint, specializing with one hand makes <b>sense</b>. Chimpanzees tend to choose a favorite hand for different tasks.”</i> <a href="https://www.bbc.com/future/article/20160930-the-mystery-of-why-left-handers-are-so-much-rarer">[24_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>сенс</b> - суть чого-небудь; зміст. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"З точки зору еволюції, домінування однієї руки цілком має <b>сенс</b>. Шимпанзе, приміром, роблять певні речі або тільки лівою рукою, або тільки правою."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-39667412">[24_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣9️⃣8️⃣ set / встановити":

    """
1️⃣9️⃣8️⃣

💫 <b>set / встановити</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 142 / частота: 39</i>

🇬🇧 <b>set</b> - to put something in a particular place or position. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Why should we expect to agree on where to <b>set</b> the boundaries, or on which colours are the most fundamental?”</i> <a href="https://www.bbc.com/future/article/20120427-when-is-a-colour-not-a-colour">[94_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>встановити</b> - ставити, поміщати десь що-небудь певним чином, підготовлюючи до використання. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Тож чому ми повинні мати однакові погляди на те, де <b>встановити</b> межу між відтінками, або який колір є домінантним серед схожих відтінків?"</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151216_vert_fut_when_is_a_colour_not_a_colour_vp">[94_BBC_Future_Corpus_UKR]</a>
    """,

    "1️⃣9️⃣9️⃣ she / вона":

    """
1️⃣9️⃣9️⃣

💫 <b>she / вона</b> 💫

🔹 <i>pronoun / займенник</i>
🔹 <i>frequency: 508 / частота: 537</i>

🇬🇧 <b>she</b> - used as the subject of a verb to refer to a woman, girl, or female animal that has already been mentioned. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“‘When I was about a week old I remember being in this pink cotton blanket,’ Rebecca Sharrock recalls. ‘I’d always know when it was Mum holding me, for some reason. I just instinctively always knew and <b>she</b> was my favourite person.’”</i> <a href="https://www.bbc.com/future/article/20171108-the-woman-who-cant-forget">[155_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>вона</b> - вживається на позначення предмета мовлення, вираженого іменником жіночого роду однини в попередньому реченні або після цього займенника. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>""Я пам'ятаю себе у віці одного тижня, мене загорнули в рожеву бавовняну ковдрочку" - згадує Ребекка Шеррок. "Я завжди знала, коли мене на руки брала мама. Я просто інстинктивно впізнавала її, <b>вона</b> мені подобалася більше за всіх"".</i> <a href="https://www.bbc.com/ukrainian/vert-fut-42344297">[155_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣0️⃣0️⃣ short / короткий":

    """
2️⃣0️⃣0️⃣

💫 <b>short / короткий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 130 / частота: 31</i>

🇬🇧 <b>short</b> - small in length, distance, or height. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“When you’re studying, it’s certainly worth taking <b>short</b> breaks to ensure that fatigue doesn’t overcome your natural abilities.”</i> <a href="https://www.bbc.com/future/article/20150429-how-to-learn-with-zero-effort">[34_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>короткий</b> - який має малу довжину; який триває недовго. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Робити <b>короткі</b> паузи під час навчання, безперечно, дуже важливо, адже вони не дозволяють втомі відволікати вашу увагу."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/01/160120_vert_fut_how_to_learn_with_zero_effort_vp">[34_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣0️⃣1️⃣ show / показувати":

    """
2️⃣0️⃣1️⃣

💫 <b>show / показувати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 256 / частота: 12</i>

🇬🇧 <b>show</b> - to make it possible for something to be seen. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“It’s important to name what you did wrong, to <b>show</b> yourself as being penitent in some way and to indicate what might be different in the future.”</i> <a href="https://www.bbc.com/future/article/20160223-why-do-the-british-say-sorry-so-much">[66_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>показувати</b> - давати можливість бачити, розглядати, роздивлятися кого-, що-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Дуже важливо назвати те, за що ви просите пробачення, щоби <b>показати</b>, що ви розкаялись і що у майбутньому все буде інакше."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/03/160301_vert_fut_why_do_the_british_say_sorry_so_much_vp">[66_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣0️⃣2️⃣ side / сторона":

    """
2️⃣0️⃣2️⃣

💫 <b>side / сторона</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 130 / частота: 12</i>

🇬🇧 <b>side</b> - a flat outer surface of an object, especially one that is not the top, the bottom, the front, or the back. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Why are some people extraordinarily selfish, manipulative, and unkind? David Robson asks the scientist delving into the darkest <b>sides</b> of the human mind.”</i> <a href="https://www.bbc.com/future/article/20150130-the-man-who-studies-evil">[54_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>сторона</b> - простір, місцевість, розташовані в якому-небудь напрямку від когось, чогось, а також цей напрямок. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Чому деякі люди надзвичайно егоїстичні, деспотичні та недоброзичливі? Кореспондент BBC Future розмовляє із науковцем, який вивчає найтемніші <b>сторони</b> людського розуму."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150811_the_man_who_studies_evil_vp">[54_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣0️⃣3️⃣ similar / подібний":

    """
2️⃣0️⃣3️⃣

💫 <b>similar / подібний</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 113 / частота: 60</i>

🇬🇧 <b>similar</b> - looking or being almost, but not exactly, the same. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“In another example, tapping your chin with your thumb twice while holding your hand with the middle-finger out is a sign for an offensive phrase involving someone’s mother since a <b>similar</b> gesture, with all five fingers straight out is the sign for ‘mother’.”</i> <a href="https://www.bbc.com/future/article/20160303-the-surprising-benefits-of-swearing">[186_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>подібний</b> - який має спільні риси з ким-, чим-небудь, схожий на когось, щось. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Подвійне постукування підборіддя великим пальцем руки з піднятим середнім пальцем означає образливу фразу, в якій згадується матір співрозмовника, бо <b>подібний</b> жест, але з піднятими догори усіма п'ятьма пальцями має значення 'матір'."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/03/160304_vert_fut_the_surprising_benefits_of_swearing_vp">[186_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣0️⃣4️⃣ simple / простий":

    """
2️⃣0️⃣4️⃣

💫 <b>simple / простий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 108 / частота: 87</i>

🇬🇧 <b>simple</b> - easy to understand or do; not difficult. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“But in the northern hemisphere at least, these findings could offer a <b>simple</b> way to kill the germs while they are still hanging in the air.”</i> <a href="https://www.bbc.com/future/article/20151016-the-real-reason-germs-spread-in-the-winter">[140_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>простий</b> - неважкий, легкий для розуміння, здійснення, виконання. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Втім, у північній півкулі, де віруси протягом деякого часу залишаються в повітрі, можна запропонувати <b>простий</b> спосіб позбутися їх."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151023_vert_fut_reason_flu_spreads_in_the_winter_vp">[140_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣0️⃣5️⃣ simply / просто":

    """
2️⃣0️⃣5️⃣

💫 <b>simply / просто</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 147 / частота: 2017</i>

🇬🇧 <b>simply</b> - in an easy way. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Allergies are not <b>simply</b> a biological blunder. Instead, they’re an essential defence against noxious chemicals – a defence that has served our ancestors for tens of millions of years and continues to do so today.”</i> <a href="https://www.bbc.com/future/article/20150409-why-do-we-have-allergies">[138_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>просто</b> - неважко, легко для розуміння, здійснення, виконання. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Алергія – це не <b>просто</b> біологічна помилка. Це важливий захист від шкідливих хімічних речовин – захист, який служив нашим предкам десятки мільйонів років тому і який продовжує робити це і сьогодні."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/08/160817_vert_fut_why_do_we_have_allergies_vp">[138_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣0️⃣6️⃣ sleep / спати":

    """
2️⃣0️⃣6️⃣

💫 <b>sleep / спати</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 320 / частота: 58</i>

🇬🇧 <b>sleep</b> - the resting state in which the body is not active and the mind is unconscious. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Stanley says that a lot of people with sleep issues actually don’t have any problem sleeping, instead they have an expectation that they need to <b>sleep</b> for a certain amount of time.”</i> <a href="https://www.bbc.com/future/article/20150706-the-woman-who-barely-sleeps">[30_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>спати</b> - перебувати у стані сну. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Ніл Стенлі також каже, що більшість людей, які мають проблеми зі сном, насправді абсолютно здорові, просто вони мають хибні очікування щодо того, скільки вони повинні <b>спати</b>."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150710_vert_fut_little_sleep_vp">[30_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣0️⃣7️⃣ small / маленький":

    """
2️⃣0️⃣7️⃣

💫 <b>small / маленький</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 232 / частота: 101</i>

🇬🇧 <b>small</b> - little in size or amount when compared with what is typical or average. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“You can enter any <b>small</b> watering hole and be treated like a long lost friend. You may not understand a word of what they say to you, but the good vibes will win you over.”</i> <a href="https://www.bbc.com/travel/article/20150529-living-in-the-worlds-safest-cities">[68_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>маленький</b> - невеликий розміром, незначний величиною. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Ви заходите у <b>маленький</b> бар, а вас зустрічають як старого друга, з яким не бачилися сто років. Нехай ви не зрозумієте ані слова з того, що вам говорять, атмосфера доброзичливості підкорює."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-40521665">[68_BBC_Travel_Corpus_UKR]</a>
    """,

    "2️⃣0️⃣8️⃣ social / соціальний":

    """
2️⃣0️⃣8️⃣

💫 <b>social / соціальний</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 232 / частота: 179</i>

🇬🇧 <b>social</b> - relating to activities in which you meet and spend time with other people and that happen during the time when you are not working. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“It’s a scientific fact that high <b>social</b> status is attractive to women.”</i> <a href="https://www.bbc.com/future/article/20161014-why-billionaires-have-more-sons">[170_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>соціальний</b> - пов'язаний із життям і стосунками людей у суспільстві. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Той факт, що високий <b>соціальний</b> статус приваблює жінок, доведений науковцями."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/10/161017_vert_fut_why_billionaires_have_more_sons_vp">[170_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣0️⃣9️⃣ someone / хтось":

    """
2️⃣0️⃣9️⃣

💫 <b>someone / хтось</b> 💫

🔹 <i>pronoun / займенник</i>
🔹 <i>frequency: 168 / частота: 75</i>

🇬🇧 <b>someone</b> - used to refer to a single person when you do not know who they are or when it is not important who they are. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“People needn’t worry about falling into a black hole, Icelanders say, because there is no black hole to fall into you. There’s always <b>someone</b> to catch you.”</i> <a href="https://www.bbc.com/travel/article/20160509-the-truth-about-icelandic-happiness">[71_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>хтось</b> - якась людина, істота. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Як кажуть самі ісландці, люди тут не бояться впасти в чорну діру, тому що чорні діри не мають можливості потрапити всередину них. Поруч завжди знайдеться <b>хтось</b>, готовий підставити плече в скрутну годину."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-41863915">[71_BBC_Travel_Corpus_UKR]</a>
    """,

    "2️⃣1️⃣0️⃣ something / щось":

    """
2️⃣1️⃣0️⃣

💫 <b>something / щось</b> 💫

🔹 <i>pronoun / займенник</i>
🔹 <i>frequency: 310 / частота: 94</i>

🇬🇧 <b>something</b> - an object, situation, quality, or action that is not exactly known or stated. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Have you ever seen or heard <b>something</b> amazing – a scene in a film, a joke or a song – only to forget it later on? Instead of the crystal clear images you wanted to recall, you’re instead left with scraps of images and mangled sentences, or more frustratingly still, nothing at all.”</i> <a href="https://www.bbc.com/future/article/20151111-improve-your-memory-in-40-seconds">[42_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>щось</b> - невизначений або невідомий предмет, якесь явище і т. ін. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Ви побачили, прочитали або почули <b>щось</b>, що вас вразило – сцена у фільмі, історія, жарт або пісня – але через деякий час ви все це геть забули. Замість чітких спогадів, які ви хотіли би зберегти в пам'яті, у вас залишились обривки образів та фраз, а іноді взагалі глуха порожнеча."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/11/151113_vert_fut_improve_your_memory_in_40_seconds_vp">[42_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣1️⃣1️⃣ sometimes / іноді":

    """
2️⃣1️⃣1️⃣

💫 <b>sometimes / іноді</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 110 / частота: 94</i>

🇬🇧 <b>sometimes</b> - on some occasions but not always or often. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“And, yes, I did bite my nails while writing this column. <b>Sometimes</b> even a good theory doesn't help.”</i> <a href="https://www.bbc.com/future/article/20140710-why-do-we-bite-our-nails">[63_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>іноді</b> - час від часу; часом, деколи, інколи. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Зізнаюсь, я гриз нігті, поки писав цю статтю. <b>Іноді</b> навіть найкращі теорії не допомагають."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150817_vert_fut_why_do_we_bite_nails_vp">[63_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣1️⃣2️⃣ space / космос":

    """
2️⃣1️⃣2️⃣

💫 <b>space / космос</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 175 / частота: 46</i>

🇬🇧 <b>space</b> - an empty area that is available to be used; the empty area outside Earth's atmosphere, where the planets and the stars are. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“We each carry a radiation monitor with us the entire time we’re in <b>space</b>… I kept that in my pocket for my entire mission, on both of my missions.”</i> <a href="https://www.bbc.com/future/article/20180208-what-its-like-in-the-bermuda-triangle-of-space">[117_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>космос</b> - сукупність усіх форм матерії як єдине ціле; уся система світобудови. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Кожен з нас має радіаційний датчик, з яким ми ніколи не розлучаємося під час перебування у <b>космосі</b>. Я тримав його у кишені під час обох місій."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-43004293">[117_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣1️⃣3️⃣ start / починати":

    """
2️⃣1️⃣3️⃣

💫 <b>start / починати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 268 / частота: 214</i>

🇬🇧 <b>start</b> - to begin doing something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“English grammar, it is best to <b>start</b> by about 10 years old, after which that ability declines”</i> <a href="https://www.bbc.com/future/article/20181024-the-best-age-to-learn-a-foreign-language">[133_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>починати</b> - приступати до якої-небудь дії, братися за якусь справу. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Вони з'ясували, що для опанування англійської граматики на рівні носія мови, <b>починати</b> вивчати її треба не пізніше 10 років. Пізніше ця здатність поступово знижується."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-45997320">[133_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣1️⃣4️⃣ story / розповідь":

    """
2️⃣1️⃣4️⃣

💫 <b>story / розповідь</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 167 / частота: 23</i>

🇬🇧 <b>story</b> - a set of connected things or devices that operate together. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Though an elaborate account, the <b>story</b> alone was not enough to make me believe this was the one true grail.”</i> <a href="https://www.bbc.com/travel/article/20180528-is-this-the-home-of-the-holy-grail">[10_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>розповідь</b> - усне, словесне повідомлення про кого-, що-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Хоча <b>розповідь</b> була досить докладною, вона не довела мені, що це - саме той, єдиний Грааль."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-44336727">[10_BBC_Travel_Corpus_UKR]</a>
    """,

    "2️⃣1️⃣5️⃣ study / вчитися":

    """
2️⃣1️⃣5️⃣

💫 <b>study / вчитися</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 663 / частота: 17</i>

🇬🇧 <b>study</b> - to learn about a subject, especially in an educational course or by reading books. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“For his part, Wannerton first brought up his strange ability to his parents when he was about 10, he says, because the distraction of constant flavours washing over him made it difficult to read and <b>study</b> for school.”</i> <a href="https://www.bbc.com/future/article/20150204-the-man-who-tastes-words">[106_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>вчитися</b> - засвоювати які-небудь знання, вивчати що-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Джеймс вперше розповів своїм батькам про свій незвичайний дар, коли йому було років десять. У той час потік різних смаків, який буквально запліскував його, заважав йому читати і <b>вчитися</b> в школі."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/01/151230_vert_fut_vert_fut_colour_tastes_good_vp">[106_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣1️⃣6️⃣ system / система":

    """
2️⃣1️⃣6️⃣

💫 <b>system / система</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 210 / частота: 207</i>

🇬🇧 <b>system</b> - a set of connected things or devices that operate together. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“But we’d have to take into account the delay in transmissions – the nearest star <b>system</b> with a planet is 10.5 light years away.”</i> <a href="https://www.bbc.com/future/article/20160223-what-would-happen-if-aliens-contacted-earth">[118_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>система</b> - порядок, зумовлений правильним, планомірним розташуванням та взаємним зв'язком частин чого-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Довелося б також зважати на затримку в обміні повідомленнями, тому що найближча до нас зоряна <b>система</b> з планетою знаходиться на відстані 10,5 світлових років."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-42011509">[118_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣1️⃣7️⃣ take / взяти":

    """
2️⃣1️⃣7️⃣

💫 <b>take / взяти</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 572 / частота: 58</i>

🇬🇧 <b>take</b> - to move something or someone from one place to another. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i><b>Taking</b> a fake hand – one of the props from the party – he placed it in front of his body while hiding his real hand from view, and he asked a friend to stroke both of the hands simultaneously.</i> <a href="https://www.bbc.com/future/article/20141107-mind-bending-body-illusions">[40_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>взяти</b> - ухопити рукою (руками) або яким-небудь знаряддям. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Він <b>взяв</b> штучну руку – один із реквізитів свята – і приладнав її до себе, а справжню руку сховав під одягом. Потім - попросив приятеля погладити обидві руки одночасно.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/06/150623_vert_fut_body_illusions_vp">[40_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣1️⃣8️⃣ team / команда":

    """
2️⃣1️⃣8️⃣

💫 <b>team / команда</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 110 / частота: 62</i>

🇬🇧 <b>team</b> - a number of people or animals who do something together as a group. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Again, these were only observational studies, but one <b>team</b> decided to put it to a test with a carefully planned intervention, feeding their participants 27%-fat Gouda cheese every day for eight weeks.</i> <a href="https://www.bbc.com/future/article/20151029-are-any-foods-safe-to-eat-anymore-heres-the-truth">[108_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>команда</b> - група людей, що виконує якусь роботу. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Знову ж таки, ці дані – лише емпіричні. Тим не менш, <b>команда</b> вчених вирішила перевірити їх за допомогою ретельно розробленого експерименту. У ході випробування його учасники мали їсти сир "Гауда" з жирністю 27% щодня впродовж восьми тижнів.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151215_vert_fut_are_any_foods_safe_to_eat_anymore_heres_the_truth_vp">[108_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣1️⃣9️⃣ term / термін":

    """
2️⃣1️⃣9️⃣

💫 <b>term / термін</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 163 / частота: 38</i>

🇬🇧 <b>term</b> - a word or expression used in relation to a particular subject, often to describe something official or technical. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>To help him in his search, Proctor enlisted the help of UC Berkeley linguist Iain Boal, and together they came up with the <b>term</b> – the neologism was coined in 1995, although much of Proctor’s analysis of the phenomenon had occurred in the previous decades.</i> <a href="https://www.bbc.com/future/article/20160105-the-man-who-studies-the-spread-of-ignorance">[115_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>термін</b> - слово або словосполучення, що означає чітко окреслене спеціальне поняття якої-небудь галузі науки, техніки, мистецтва, суспільного життя тощо. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Колегою і співробітником професора Проктора став лінгвіст з Каліфорнійського університету в Берклі Айн Боаль, разом з яким вони у 1995 році вигадали <b>термін</b> "агнотологія", хоча значну частину дослідження Роберт Проктор виконав раніше.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/02/160209_vert_fut_the_man_who_studies_the_spread_of_ignorance_vp">[115_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣2️⃣0️⃣ then / потім":

    """
2️⃣2️⃣0️⃣

💫 <b>then / потім</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 398 / частота: 141</i>

🇬🇧 <b>then</b> - (at) that time (in the past or in the future). <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>And <b>then</b> I looked at the map and hesitated, realizing what I was about to do. If everything went as promised, I would rocket 30km away from my boarding gate.</i> <a href="https://www.bbc.com/travel/article/20170125-a-high-speed-getaway-like-no-other">[58_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>потім</b> - після чого-небудь (для позначення послідовності у часі). <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i><b>Потім</b> я глянув на мапу і завагався, усвідомивши, що збираюся зробити. Якщо все піде за планом, моя подорож туди і назад, довжиною в 60 км, триватиме менше ніж 20 хвилин.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-38904380">[58_BBC_Travel_Corpus_UKR]</a>
    """,

    "2️⃣2️⃣1️⃣ theory / теорія":

    """
2️⃣2️⃣1️⃣

💫 <b>theory / теорія</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 133 / частота: 114</i>

🇬🇧 <b>theory</b> - a formal statement of the rules on which a subject of study is based or of ideas that are suggested to explain a fact or event or, more generally, an opinion or explanation. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Allergies are not simply a biological blunder. Instead, they’re an essential defence against noxious chemicals – a defence that has served our ancestors for tens of millions of years and continues to do so today. It’s a controversial <b>theory</b>, Medzhitov acknowledges.</i> <a href="https://www.bbc.com/future/article/20150409-why-do-we-have-allergies">[138_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>теорія</b> - логічне узагальнення досвіду, суспільної практики, яке ґрунтується на глибокому проникненні в суть досліджуваного явища та розкриває його закономірності. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Алергія – це не просто біологічна помилка. Це важливий захист від шкідливих хімічних речовин – захист, який служив нашим предкам десятки мільйонів років тому і який продовжує робити це і сьогодні. Це суперечлива <b>теорія</b>, визнає вчений.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/08/160817_vert_fut_why_do_we_have_allergies_vp">[138_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣2️⃣2️⃣ there / там":

    """
2️⃣2️⃣2️⃣

💫 <b>there / там</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 1129 / частота: 65</i>

🇬🇧 <b>there</b> - (to, at, or in) that place. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>What happens <b>there</b>? The CIA won’t give specifics, which is why the site’s purpose is rife with conspiracy theories.</i> <a href="https://www.bbc.com/travel/article/20160225-the-worlds-most-secretive-places">[06_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>там</b> - уживається при вказуванні на місце більш віддалене порівняно з іншим, ближчим. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Що ж <b>там</b> відбувається? ЦРУ не розкриває жодних деталей, і це суттєво підживлює фантазію прихильників теорій змови.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-40557407">[06_BBC_Travel_Corpus_UKR]</a>
    """,

    "2️⃣2️⃣3️⃣ they / вони":

    """
2️⃣2️⃣3️⃣

💫 <b>they / вони</b> 💫

🔹 <i>pronoun / займенник</i>
🔹 <i>frequency: 2149 / частота: 1087</i>

🇬🇧 <b>they</b> - used as the subject of a verb to refer to people, animals, or things already mentioned or, more generally, to a group of people not clearly described. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“At this age, children don’t learn a language – <b>they</b> acquire it,” says the school’s director Carmen Rampersad. It seems to sum up the enviable effortlessness of the little polyglots around her.</i> <a href="https://www.bbc.com/future/article/20181024-the-best-age-to-learn-a-foreign-language">[133_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>вони</b> - уживається на позначення предмета мовлення, вираженого іменником у множині до або після цього займенника. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"У цьому віці діти не вивчають мову - <b>вони</b> її набувають", - каже директорка садку Кармен Рамперсад. Те, з якою легкістю маленькі поліглоти навколо підхоплюють мову, виглядає найкращою ілюстрацією її слів.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-45997320">[133_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣2️⃣4️⃣ thing / річ":

    """
2️⃣2️⃣4️⃣

💫 <b>thing / річ</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 377 / частота: 25</i>

🇬🇧 <b>thing</b> - used to refer in an approximate way to an idea, subject, event, action, etc. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Alter one <b>thing</b>, and you could alter everything and end up rewriting reality.”</i> <a href="https://www.bbc.com/future/article/20150216-the-truth-about-movie-time-travel">[67_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>річ</b> - явище дійсності, вияв або результат якої-небудь дії, діяльності. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Зміниш одну <b>річ</b> - і вся реальність може стати іншою."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/10/151022_vert_fut_the_truth_about_movie_time_travel_vp">[67_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣2️⃣5️⃣ think / думати":

    """
2️⃣2️⃣5️⃣

💫 <b>think / думати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 711 / частота: 119</i>

🇬🇧 <b>think</b> - to believe something or have an opinion or idea. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Indeed, once you start <b>thinking</b> about all the different kinds of information reaching the human brain, you might even find that you develop a brand new sense – a radar-like sensitivity to some of the other misconceptions regarding the way the brain experiences the world.”</i> <a href="https://www.bbc.com/future/article/20141118-how-many-senses-do-you-have">[61_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>думати</b> - розмірковувати над чим-небудь; мислити. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Насправді, коли починаєш <b>думати</b> про все розмаїття інформації, яка туди потрапляє, можна легко вигадати ще одне нове чуття – своєрідний радар стереотипів і міфів, які оточують наш мозок."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150917_vert_fut_how_many_senses_do_you_have_vp">[61_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣2️⃣6️⃣ thought / думка":

    """
2️⃣2️⃣6️⃣

💫 <b>thought / думка</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 232 / частота: 268</i>

🇬🇧 <b>thought</b> - the act of thinking about or considering something, an idea or opinion, or a set of ideas about a particular subject. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“And Icelanders certainly recognise the value of the written word, an attitude reflected in a common Icelandic saying: ‘Better to go barefoot than without books.’ A happy <b>thought</b>, if ever there were one.”</i> <a href="https://www.bbc.com/travel/article/20160509-the-truth-about-icelandic-happiness">[71_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>думка</b> - те, що з'явилося в результаті міркування, продукт мислення. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"А от написане слово ісландці дійсно вміють цінувати, як свідчить поширена тут приказка: 'Краще босоніж - та з книгою'. Якщо <b>думки</b> можуть притягувати щастя, то це - точно одна з них."</i> <a href="https://www.bbc.com/ukrainian/vert-tra-41863915">[71_BBC_Travel_Corpus_UKR]</a>
    """,

    "2️⃣2️⃣7️⃣ time / час":

    """
2️⃣2️⃣7️⃣

💫 <b>time / час</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 842 / частота: 962</i>

🇬🇧 <b>time</b> - the part of existence that is measured in minutes, days, years, etc., or this process considered as a whole. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“The most natural <b>time</b> to nap, based on our circadian rhythms, is between 2 and 4pm.”</i> <a href="https://www.bbc.com/future/article/20150710-what-you-may-not-know-about-sleep">[29_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>час</b> - одна з основних об'єктивних форм існування матерії, яка виявляється в тривалості буття. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Аналіз добових біоритмів людини показує, що найбільш природний <b>час</b> для денного сну – між 14.00 та 16.00 годинами."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150803_vert_fut_what_you_may_not_know_about_sleep_vp">[29_BBC_Future_Corpus_UKR]</a>
    """,

   "2️⃣2️⃣8️⃣ today / сьогодні":

    """
2️⃣2️⃣8️⃣

💫 <b>today / сьогодні</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 174 / частота: 154</i>

🇬🇧 <b>today</b> - (on) the present day. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“In general, however, we shouldn’t feel hostile towards these invaders – after all, they made you who you are <b>today</b>.”</i> <a href="https://www.bbc.com/future/article/20150917-is-another-human-living-inside-you">[87_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>сьогодні</b> - у цей, нинішній день (між учорашнім і завтрашнім днем). <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Насправді, ми не мусимо вороже ставитися до цих 'загарбників'. Зрештою, вони зробили нас тими, ким ми є <b>сьогодні</b>."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150922_vert_fut_another_human_living_inside_you_vp">[87_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣2️⃣9️⃣ true / правдивий":

    """
2️⃣2️⃣9️⃣

💫 <b>true / правдивий</b> 💫

🔹 <i>adjective / прикметник</i>
🔹 <i>frequency: 122 / частота: 8</i>

🇬🇧 <b>true</b> - (especially of facts or statements) right and not wrong; correct. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“At face value, the myth of the beer belly should be <b>true</b>. Alcohol itself contains calories, not to mention all the sugars that make our favourite drinks so tasty.”</i> <a href="https://www.bbc.com/future/article/20151026-is-beer-better-or-worse-for-you-than-wine">[197_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>правдивий</b> - який відповідає правді, істині. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"На перший погляд, міф про пивний живіт здається <b>правдивим</b>. Алкоголь і сам по собі містить калорії, не кажучи вже про цукор, який додають в наші улюблені напої, щоби зробити їх ще смачнішими."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/11/151106_vert_fut_is_beer_better_or_worse_for_you_than_wine_vp">[197_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣3️⃣0️⃣ try / намагатися":

    """
2️⃣3️⃣0️⃣

💫 <b>try / намагатися</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 270 / частота: 8</i>

🇬🇧 <b>try</b> - to attempt to do something. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“‘Your phone’s approach to existence is to broadcast continuously on every available open channel: ‘I’m here! Over here! It’s meeee!’ – and to <b>try</b> and connect to any signals it can,” says the Data Detox Kit.</i> <a href="https://www.bbc.com/future/article/20171110-the-8-day-guide-to-a-better-digital-life">[195_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>намагатися</b> - пробувати робити що-небудь; докладати зусиль до чого-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Ваш смартфон із самого початку налаштований на те, щоби повідомляти про свою присутність на кожному доступному каналі: 'Я тут! Ось я! Це - яяяяя!' і <b>намагатися</b> підключитися до кожного сигналу", - розповідає Data Detox.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-41999571">[195_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣3️⃣1️⃣ understand / розуміти":

    """
2️⃣3️⃣1️⃣

💫 <b>understand / розуміти</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 169 / частота: 99</i>

🇬🇧 <b>understand</b> - to know the meaning of something that someone says. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Luck, though, seemed to have found 17-year-old Nicole Moss of Tooting, who is at her first auction – and is now the proud owner of Chanel shoes and a Chanel dress. ‘I don’t <b>understand</b> why people leave such nice things,’ she says.”</i> <a href="https://www.bbc.com/future/article/20150907-did-an-airline-auction-off-your-luggage">[76_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>розуміти</b> - сприймати, осягати розумом. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"А ось 17-річній Ніколь Мосс із Тутінга дуже пощастило. Це її перший аукціон, і вона вже стала гордою власницею черевиків і сукні від Chanel. 'Не <b>розумію</b>, як люди можуть відмовлятися від таких чудових речей', – каже вона."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/09/150909_vert_fut_did_an_airline_auction_off_your_luggage_vp">[76_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣3️⃣2️⃣ university / університет":

    """
2️⃣3️⃣2️⃣

💫 <b>university / університет</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 376 / частота: 326</i>

🇬🇧 <b>university</b> - a place where people study for an undergraduate (= first) or postgraduate (= higher level) degree. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“Incredibly it wasn’t until the 15th Century that zero, along with all the other Arabic numbers, was finally accepted. Just to put it in context, by then Oxford <b>University</b> in England had been around for centuries and the printing press was just up and running.”</i> <a href="https://www.bbc.com/future/article/20161206-we-couldnt-live-without-zero-but-we-once-had-to">[25_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>університет</b> - вищий навчальний заклад, наукова установа з різними гуманітарними та природничо-математичними факультетами. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Неймовірно, але нуль, як і всі арабські цифри, остаточно визнали лише в XV столітті. Щоб зрозуміти контекст, подумайте, що на той час Оксфордський <b>університет</b> існував вже кілька століть, а завдяки друкарству вже повним ходом поширювалися книжки."</i> <a href="https://www.bbc.com/ukrainian/vert-fut-38253161">[25_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣3️⃣3️⃣ use / використовувати":

    """
2️⃣3️⃣3️⃣

💫 <b>use / використовувати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 723 / частота: 85</i>

🇬🇧 <b>use</b> - to put something such as a tool, skill, or building to a particular purpose. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“‘Euskara has been <b>used</b> as a weapon. It has become politicised and manipulated,’ Errekatxo said. ‘There’s the perception that Euskara belongs to the nationalists. I believe a language is universal.’”</i> <a href="https://www.bbc.com/travel/article/20170719-the-mysterious-origins-of-europes-oldest-language">[28_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>використовувати</b> - застосовувати, вживати що-небудь з користю, користуватися чимсь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"'Баскську мову почали <b>використовувати</b> як зброю. Вона стала політизованою, нею маніпулювали,' - каже Еррекатчо. 'Дехто вважає баскську - мовою націоналістів, але я впевнена, що мова є універсальною.'"</i> <a href="https://www.bbc.com/ukrainian/vert-tra-40729382">[28_BBC_Travel_Corpus_UKR]</a>
    """,

    "2️⃣3️⃣4️⃣ very / дуже":

    """
2️⃣3️⃣4️⃣

💫 <b>very / дуже</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 348 / частота: 382</i>

🇬🇧 <b>very</b> - (used to add emphasis to an adjective or adverb) to a great degree or extremely. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>“There are, of course, two <b>very</b> different reasons why people wear glasses – short-sightedness, or myopia, where things in the distance are blurry; and long-sightedness, or hyperopia, where you can’t focus on things close up.”</i> <a href="https://www.bbc.com/future/article/20140513-do-glasses-weaken-your-eyesight">[182_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>дуже</b> - у великій мірі, надто, надзвичайно. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Існують дві <b>дуже</b> різні причини, чому люди носять окуляри. Одна з них це – міопія або короткозорість, коли об'єкти на відстані виглядають розмитими. Інша – гіперметропія або далекозорість, коли вам важко сфокусувати зір на предметах, що розташовані поруч."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2016/06/160624_vert_fut_do_spectacles_worsen_sight_vp">[182_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣3️⃣5️⃣ want / хотіти":

    """
2️⃣3️⃣5️⃣

💫 <b>want / хотіти</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 255 / частота: 59</i>

🇬🇧 <b>want</b> - to wish for a particular thing or plan of action. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>"I <b>want</b> to walk my daughter down the aisle and remember it. Should they become parents, I would like to remember that I have grandchildren, and who they are."</i> <a href="https://www.bbc.com/future/article/20150630-my-dentist-saved-my-tooth-but-stole-my-memory">[45_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>хотіти</b> - мати бажання, охоту до чогось, відчувати потребу в чому-небудь. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>"Я <b>хочу</b> повести доньку під вінець і запам'ятати це. А коли мої діти стануть батьками, я хочу пам'ятати, що в мене є внуки, і які вони."</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/08/150820_vert_fut_dentist_extracted_memory_vp">[45_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣3️⃣6️⃣ water / вода": 
    
    """
2️⃣3️⃣6️⃣

💫 <b>water / вода</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 155 / частота: 131</i>

🇬🇧 <b>water</b> - a clear liquid, without colour or taste, that falls from the sky as rain and is necessary for animal and plant life. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>If the <b>water</b> is very hot or very cold, then we tend not to wash our hands for long. Just showing our hands the water isn’t enough, and some nice warm water might encourage us to tarry a while by the wash basin.</i> <a href="https://www.bbc.com/future/article/20170519-does-it-matter-how-you-wash-and-dry-your-hands">[18_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>вода</b> - прозора, безбарвна рідина, що становить собою найпростішу хімічну сполуку водню з киснем. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Якщо <b>вода</b> буде надто холодною або надто гарячою, ми не триматимемо руки під краном достатньо довго, щоби змити усі бактерії. А приємно тепла вода сприятиме тому, що ми проведемо біля вмивальника трохи більше часу.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-40015296">[18_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣3️⃣7️⃣ way / шлях": 
    
    """
2️⃣3️⃣7️⃣

💫 <b>way / шлях</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 629 / частота: 91</i>

🇬🇧 <b>way</b> - a route, direction, or path. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>After greeting each other, Nan-in asked Teno: “Did you leave your umbrella to the left or right of your clogs?” Unable to answer, Teno realised he was still a long <b>way</b> from attaining Zen, and went away to study for six more years.</i> <a href="https://www.bbc.com/travel/article/20170504-the-japanese-skill-copied-by-the-world">[70_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>шлях</b> - смуга землі, призначена для їзди та ходіння. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Після обміну вітаннями Нань-ін запитав Тено: "Ти залишив парасолю зліва чи справа від сандалів?" Не пам'ятаючи цього, Тено зрозумів, що для досягнення дзен йому потрібно пройти ще великий <b>шлях</b>. Він пішов і навчався ще шість років.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-42286751">[70_BBC_Travel_Corpus_UKR]</a>
    """,

    "2️⃣3️⃣8️⃣ we / ми": 
    
    """
2️⃣3️⃣8️⃣

💫 <b>we / ми</b> 💫

🔹 <i>pronoun / займенник</i>
🔹 <i>frequency: 1853 / частота: 1173</i>

🇬🇧 <b>we</b> - used as the subject of a verb to refer to a group including the speaker and at least one other person. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>This matters because, unfortunately, <b>we</b> can’t resist touching our faces, allowing germs to spread nicely from our hands to our noses and mouths, where they can get into the body.</i> <a href="https://www.bbc.com/future/article/20170519-does-it-matter-how-you-wash-and-dry-your-hands">[18_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>ми</b> - вживається для називання двох чи багатьох осіб разом з тим, хто говорить. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>На жаль, <b>ми</b> не можемо не торкатися нашого обличчя, і таким чином мікроби з рук потрапляють у рот чи ніс, а звідти всередину організму.</i> <a href="https://www.bbc.com/ukrainian/vert-fut-40015296">[18_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣3️⃣9️⃣ while / поки": 
    
    """
2️⃣3️⃣9️⃣

💫 <b>while / поки</b> 💫

🔹 <i>adverb / прислівник</i>
🔹 <i>frequency: 421 / частота: 137</i>

🇬🇧 <b>while</b> - during the time that, or at the same time as. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>She needs only four hours sleep a night, so has a lot of spare time to fill <b>while</b> the rest of the world is in the land of nod.</i> <a href="https://www.bbc.com/future/article/20150706-the-woman-who-barely-sleeps">[30_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>поки</b> - у даний момент, зараз. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Вона спить лише 4 години вночі і має багато вільного часу, <b>поки</b> інша частина людства перебуває в обіймах Морфею.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150710_vert_fut_little_sleep_vp">[30_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣4️⃣0️⃣ woman / жінка": 
    
    """
2️⃣4️⃣0️⃣

💫 <b>woman / жінка</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 238 / частота: 192</i>

🇬🇧 <b>woman</b> - an adult female human being. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>In 2009, a <b>woman</b> came into Ying-Hui Fu’s lab at the University of California, San Francisco, complaining that she always woke up too early.</i> <a href="https://www.bbc.com/future/article/20150706-the-woman-who-barely-sleeps">[30_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>жінка</b> - особа жіночої статі. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>У 2009 році в лабораторію професора Ін-Хой Фу в Каліфорнійському університеті міста Сан-Франциско прийшла <b>жінка</b> зі скаргою, що вона дуже рано прокидається.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150710_vert_fut_little_sleep_vp">[30_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣4️⃣1️⃣ word / слово": 
    
    """
2️⃣4️⃣1️⃣

💫 <b>word / слово</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 448 / частота: 335</i>

🇬🇧 <b>word</b> - a single unit of language that has meaning and can be spoken or written. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>As you'd expect from this theory, there's some evidence that people respond quicker to negative <b>words</b>.</i> <a href="https://www.bbc.com/future/article/20140728-why-is-all-the-news-bad">[81_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>слово</b> - мовна одиниця, що являє собою звукове вираження поняття про предмет або явище об'єктивного світу. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Не суперечить цій теорії і той факт, що люди швидше реагують на <b>слова</b> з негативним значенням.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151217_vert_fut_why_is_all_the_news_bad_vp">[81_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣4️⃣2️⃣ work / працювати": 
    
    """
2️⃣4️⃣2️⃣

💫 <b>work / працювати</b> 💫

🔹 <i>verb / дієслово</i>
🔹 <i>frequency: 419 / частота: 60</i>

🇬🇧 <b>work</b> - an activity, such as a job, that a person uses physical or mental effort to do, usually for money. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>Osaka is known for being business-focussed, which means that people <b>work</b> and commute late into the night.</i> <a href="https://www.bbc.com/travel/article/20150529-living-in-the-worlds-safest-cities">[68_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>працювати</b> - затрачати фізичну й розумову енергію, брати участь у створенні матеріальних і духовних цінностей. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Життя в Осаці зосереджене на бізнесі. Це означає, що людям доводиться <b>працювати</b> й користуватися громадським транспортом до глибокої ночі.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-40521665">[68_BBC_Travel_Corpus_UKR]</a>
    """,

    "2️⃣4️⃣3️⃣ world / світ": 
    
    """
2️⃣4️⃣3️⃣

💫 <b>world / світ</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 493 / частота: 448</i>

🇬🇧 <b>world</b> - the earth and all the people, places, and things on it. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>There's another interpretation that Trussler and Soroka put on their evidence: we pay attention to bad news, because on the whole, we think the <b>world</b> is rosier than it actually is.</i> <a href="https://www.bbc.com/future/article/20140728-why-is-all-the-news-bad">[81_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>світ</b> - сукупність усіх форм матерії як єдине ціле. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Дослідники Трасслер і Сорока пропонують й інше пояснення результатам досліду. Вчені вважають, що ми звертаємо увагу на погані новини, бо в цілому сприймаємо <b>світ</b> більш оптимістичним, ніж він є насправді.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/12/151217_vert_fut_why_is_all_the_news_bad_vp">[81_BBC_Future_Corpus_UKR]</a>
    """,

    "2️⃣4️⃣4️⃣ year / рік": 
    
    """
2️⃣4️⃣4️⃣

💫 <b>year / рік</b> 💫

🔹 <i>noun / іменник</i>
🔹 <i>frequency: 741 / частота: 929</i>

🇬🇧 <b>year</b> - a period of twelve months, especially from 1 January to 31 December. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>I'd only been living in Amsterdam for a <b>year</b> when we met my husband’s friends in one of the many cafes and bars in the city’s famous Vondelpark.</i> <a href="https://www.bbc.com/travel/article/20180131-where-dutch-directness-comes-from">[64_BBC_Travel_Corpus_ENG]</a>

🇺🇦 <b>рік</b> - одиниця літочислення, проміжок часу, близький до періоду одного обертання Землі навколо Сонця; має 12 календарних місяців. <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Я прожила в Амстердамі десь <b>рік</b>, коли одного дня ми з чоловіком домовилися зустрітися з його друзями в одному з численних кафе парку Вондела.</i> <a href="https://www.bbc.com/ukrainian/vert-tra-43128149">[64_BBC_Travel_Corpus_UKR]</a>
    """,

    "2️⃣4️⃣5️⃣ you / ти": 
    
    """
2️⃣4️⃣5️⃣

💫 <b>you / ти</b> 💫

🔹 <i>pronoun / займенник</i>
🔹 <i>frequency: 2622 / частота: 43</i>

🇬🇧 <b>you</b> - used to refer to the person or people being spoken or written to. <a href="https://dictionary.cambridge.org">[Cambridge Dictionary]</a>
📌 <i>The secret, apparently, is to linger on your chosen card as <b>you</b> riffle through the deck.</i> <a href="https://www.bbc.com/future/article/20150324-the-hidden-tricks-of-persuasion">[57_BBC_Future_Corpus_ENG]</a>

🇺🇦 <b>ти</b> - уживається при звертанні до однієї особи (звичайно близької, а також до будь-якої особи в грубому, фамільярному плані). <a href="https://sum.in.ua">[Словник української мови]</a>
📌 <i>Секрет в тому, щоб змусити учасника обрати саме ту карту з колоди, яку <b>ти</b> вже приготував у кишені.</i> <a href="https://www.bbc.com/ukrainian/vert_fut/2015/07/150717_vert_fut_the_hidden_tricks_of_persuasion_vp">[57_BBC_Future_Corpus_UKR]</a>
    """
}

# Command /wordlist to show the wordlist
async def wordlist_command(update: Update, context: CallbackContext):
    # Ensure 'current_page' is initialized in user_data
    context.user_data.setdefault('current_page', 1)

    # Calculate start and end indices for the current page
    start_index = (context.user_data['current_page'] - 1) * 10
    end_index = start_index + 10

    # Extract words on the current page
    words_on_page = list(word_definitions.keys())[start_index:end_index]

    # Initialize an empty list for keyboard
    keyboard = []

    # Add buttons for each word on the current page
    for word in words_on_page:
        button = InlineKeyboardButton(text=word, callback_data=word)
        keyboard.append([button])

    # Add navigation buttons for pagination
    prev_button = InlineKeyboardButton("⬅️ Previous", callback_data="prev")
    next_button = InlineKeyboardButton("Next ➡️", callback_data="next")
    keyboard.append([prev_button, next_button])

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Use context.bot.send_message instead of update.message.reply_text
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"🔸<b>THE WORD LIST - Page {context.user_data['current_page']}</b>🔸",
        reply_markup=reply_markup,
        parse_mode='HTML',
        disable_web_page_preview=True
    )

# Show dictionary entries
async def word_definition(update: Update, context: CallbackContext):
    query = update.callback_query
    word = query.data

    if word == "prev":
        # Navigate to the previous page
        context.user_data['current_page'] = max(1, context.user_data.get('current_page', 1) - 1)
        await wordlist_command(update, context)
    elif word == "next":
        # Navigate to the next page
        total_pages = len(word_definitions) // 10 + (len(word_definitions) % 10 > 0)
        context.user_data['current_page'] = min(total_pages, context.user_data.get('current_page', 1) + 1)
        await wordlist_command(update, context)
    else:
        # Display the definition for the selected word
        definition = word_definitions.get(word)

        if definition:
            await query.edit_message_text(text=definition, parse_mode='HTML', disable_web_page_preview=True)
        else:
            await query.edit_message_text(text="There is no such a definition", disable_web_page_preview=True)


# Command /start
async def start_command(update: Update, context: CallbackContext):
    context.user_data['current_page'] = 1
    text = (
        "Привіт! Я словниковий бот <b>LinguaLex Bot</b> або просто <b>Лексі</b> 💜\n"
        "\n"
        "Тут ви можете переглянути <b>словникові статті</b>, створені на основі корпусу <b>статей BBC</b>.\n"
        "\n"
        "Для отримання додаткової інформації, будь ласка, натисніть команду <b>/help</b>.\n"
        "\n"
        "<b>До зустрічі!</b> 👋🏻\n"
    )
    # Use context.bot.send_message instead of update.message.reply_html
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode='HTML', disable_web_page_preview=True)

# Command /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_part1 = (
        "🟣 <b>Словникові статті:</b>\n"
        "\n"
        "Кожна словникова стаття складається з наступного:\n"
        "🔸 англійське слово;\n"
        "🔸 частина мови англійського слова;\n"
        "🔸 загальна частота англійського слова;\n"
        "🔸 визначення англійського слова;\n"
        "🔸 приклад використання англійського слова з корпусу;\n"
        "🔸 українське слово;\n"
        "🔸 частина мови українського слова;\n"
        "🔸 загальна частота українського слова;\n"
        "🔸 визначення українського слова;\n"
        "🔸 приклад використання українського слова з корпусу.\n"
        "\n"
    )

    text_part2 = (
        "Цей словник налічує <b>245 словникових статей</b>, які містять лише повнозначні частини мови:\n"
        "🔹 <i>101 іменників;</i>\n"
        "🔹 <i>78 дієслів;</i>\n"
        "🔹 <i>28 прикметників;</i>\n"
        "🔹 <i>27 прислівників;</i>\n"
        "🔹 <i>11 займенників.</i>\n"
        "\n"
        "📌 <b>Загальна частота</b> кожного слова була взята з паралельних корпусів (див. нижче)\n"
        "\n"
        "📌 <b>Визначення до англійських слів</b> були взяті з <b><a href='https://dictionary.cambridge.org'>Cambridge Dictionary</a></b>\n"
        "\n"
        "📌 <b>Визначення до українських слів</b> були взяті з <b><a href='https://sum.in.ua'>Словника української мови</a></b>\n"
        "\n"
        "📌 <b>Приклади використання</b> до кожного слова були взяті також з паралельних корпусів (див. нижче)\n"
        "\n"
    )

    text_part3 = (
        "🟣 <b>Корпус текстів:</b>\n"
        "\n"
        "📌 Корпус текстів створений на основі оригіналів статей та їх перекладів з <b>BBC Travel</b> та <b>BBC Future</b>.\n"
        "\n"
        "📌 Біля кожного речення-прикладу міститься <b>пряме посилання на сайт статті</b>, куди можна перейти, натиснувши на нього.\n"
        "\n"
        "📌 Якщо Ви хочете переглянути <b>загальний список статей</b>, будь ласка, натисніть <b><a href='https://docs.google.com/spreadsheets/d/1CcfJil80hzNLY5xwSgy4h5pdrCA7XTe5DfDqmxnxQ_8/edit?usp=sharing'>тут</a></b>.\n"
        "\n"
        "📌 Корпус текстів був створений за допомогою програми <b><a href='https://www.laurenceanthony.net/software/antconc/'>AntConc</a></b>. Якщо Ви також бажаєте створити такий корпус, Ви можете завантажити статті у форматі <i>.txt</i> <b><a href='https://drive.google.com/drive/folders/1vwRNkQfSWg0zZCJ30Xnli8eB2MTgV4CM?usp=sharing'>тут</a></b>.\n"
        "\n"
        "🟣 <b>Відгуки, зауваження, пропозиції:</b>\n"
        "\n"
        "🙋🏼‍♀️ Автором цього боту є <b>Наталія Паламарчук</b>. \n"
        "\n"
        "Буду вдячна за будь-який зворотній зв’язок:\n"
        "🔹 напряму в Телеграмі: https://t.me/nataliiaaapal\n"
        "🔹 за допомогою електронної пошти: nataliakov2001@gmail.com\n"
        "\n"
        "✅ Телеграм-бот створено в рамках написання кваліфікаційної роботи на тему <b>«Діалогова система-тренажер лексичних одиниць англійської та української мов на основі телеграм-бота»</b>.\n"
        "🏫 Житомирський державний університет імені Івана Франка\n"
        "👩🏼‍🎓 <i>Науковий керівник:</i> доцент, кандидат філологічних наук <b>Чумак Людмила Миколаївна</b>.\n"
        "\n"
        "© Наталія Паламарчук, Людмила Чумак 2023-2024\n"
        "<b>Усі права захищено</b>\n"
    )

    # Concatenate all parts
    full_text = text_part1 + text_part2 + text_part3

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=full_text,
        parse_mode='HTML',
        disable_web_page_preview=True
    )

# Responses
def handle_response(text: str) -> str:

    processed_text: str = text.lower()

    return "I don't understand what you wrote... 😔"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    # React to group messages only if users mention the bot directly
    if message_type == "group":
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return  # We don't want the bot respond if it's not mentioned in the group
    else:
        response: str = handle_response(text)

    # Reply normal if the message is in private
    print("Bot:", response)
    await update.message.reply_text(response)


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


# Run the program
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("wordlist", wordlist_command))
    
    app.add_handler(CallbackQueryHandler(word_definition))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)

    print("Polling...")
    # Run the bot
    app.run_polling(poll_interval = 3)