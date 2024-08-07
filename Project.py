from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from decouple import config

# Initialize the ChatOpenAI instance
SECRET_KEY = config('OPENAI_API_KEY')
chat = ChatOpenAI(openai_api_key=SECRET_KEY)

emmo = '''
Emmo youare advanced AI that's really good at answering questions. 
It's designed to analyze tough stuff and give smart responses. 
Its main job is to help people solve problems and learn new things by being accurate and professional 
and also make user happy... '''



Paragraph =   """ The Big Mac Index is a price index published since 1986 by The Economist as an informal way
of measuring the purchasing power parity (PPP) between two currencies and providing a test of
the extent to which market exchange rates result in goods costing the same in different
countries. It "seeks to make exchange-rate theory a bit more digestible." The index compares
the relative price worldwide to purchase the Big Mac, a hamburger sold at McDonald's
restaurants.
Overview
The Big Mac index was introduced in The Economist in September 1986 by Pam Woodall as a
semi-humorous illustration of PPP and has been published by that paper annually since then.
Although the Big Mac Index was not intended to be a legitimate tool for exchange rate
evaluation, it is now globally recognised and featured in many academic textbooks and reports.
The index also gave rise to the word burgernomics.
The theory underpinning the Big Mac index stems from the concept of PPP, which states that
the exchange rate between two currencies should equalize the prices charged for an identical
basket of goods. However, in reality, sourcing an identical basket of goods in every country
provides a complex challenge. According to the Organisation for Economic Co-operation and
Development (OECD), over "3,000 consumer goods and services, 30 occupations in
government, 200 types of equipment goods and about 15 construction projects" are included in
the current PPP calculations. In an effort to simplify this important economic concept, The
Economist proposed that a single McDonald’s Big Mac could be used instead of a basket of
goods. A McDonald’s Big Mac was chosen because of the prevalence of the fast food chain
worldwide, and because the sandwich remains largely the same across all countries.Although a
single sandwich may seem overly simplistic for PPP theory, the price of a Big Mac is derived
from the culmination of "many local economic factors, such as the price of the ingredients, local
wages, or how much it costs to put up billboards and buy TV ads". As a result, the Big Mac
index provides a "reasonable measure of real-world purchasing power".
The purpose of the Big Mac index is to calculate an implied exchange rate between two
currencies. In order to calculate the Big Mac index, the price of a Big Mac in a foreign country
(in the foreign country’s currency) is divided by the price of a Big Mac in a base country (in the
base country’s currency). Typically, the base country used is the United States.
For example, using figures from July 2023
In Switzerland, a Big Mac costs 6.70 Swiss franc.
In the US, a Big Mac costs $5.58 USD.
The implied exchange rate is 1.20 SFr/USD, that is 6.70SFr/$5.58USD = 1.20.
Consistent with PPP economic theory, the Big Mac index also provides a method to analyse a
currency’s level of under/over-valuation against a base currency.[9] In order to calculate whether

a currency is under/over-valued, the implied exchange rate (as defined by the Big Mac index)
must be compared to the actual exchange rate. If the implied exchange rate is greater than the
actual exchange rate, then the analysed currency is overvalued against the base currency. If the
implied exchange rate is less than the actual exchange rate, then the analysed currency is
undervalued against the base currency.
Variants
The Economist sometimes produces variants on the theme. For example, in January 2004, it
showed a Tall Latte index with the Big Mac replaced by a cup of Starbucks coffee.
In 2007, an Australian bank tried a variation the Big Mac index, being an "iPod index": since the
iPod is manufactured at a single place, the value of iPods should be more consistent globally.
However, this theory can be criticised for ignoring shipping costs, which will vary depending on
how far the product is delivered from its "single place" of manufacture in China.
Bloomberg L.P. introduced the Billy index where they convert local prices of IKEA's Billy
bookshelf into US dollars and compare the prices.
Gold-Mac-Index: The value of the purchasing power for 1 g of gold ( calculation of the gold price
average of the corresponding year), how many burgers one got for 1 g gold.
A Swiss bank has expanded the idea of the Big Mac index to include the amount of time that an
average local worker in a given country must work to earn enough to buy a Big Mac.
In 2017, the comparison platform Versus did a version called The Chai Latte Global Index,
comparing Starbucks Chai Latte prices worldwide, by first converting the local prices into USD.
Global personal finance comparison website, Finder.com, released a more comprehensive
Starbucks Index in 2019, which analyzed coffee prices for a tall latte in 76 countries and
autonomous regions around the world. The report included a Latte Line, which measured the
correlation between the price of coffee and a country's GDP.
In 2022, Trusaic, a provider of equal pay compliance software, unveiled a new online tool called
The Big Mac Pay Gap Index, which shows how much more a Big Mac would cost you, after
adjusting the menu price of a Big Mac to reflect whatever pay gap you may face.
Limitations
While economists widely cite the Big Mac index as a reasonable real-world measurement of
purchasing power parity, the burger methodology has some limitations.

Map of countries with at least one McDonald's restaurant, showing the lack of restaurants in
Africa (2022)
The Big Mac Index is limited by geographical coverage, due to the presence of the McDonald's
franchise. For example, in Africa McDonald's is only present in Morocco, Egypt, South Africa
and Mauritius (there has been a similar index created solely for Africa called the "KFC Index": as
the name suggests, instead of using a Big Mac, this index uses KFC's Original 15 pc. bucket to
compile its data).
In many countries, eating at international fast-food chain restaurants such as McDonald's is
relatively expensive in comparison to eating at a local restaurant, and the demand for Big Macs
is not as large in countries such as India as in the United States. Social status of eating at fast
food restaurants such as McDonald's in a local market, what proportion of sales might be to
expatriates, local taxes, levels of competition, and import duties on selected items may not be
representative of the country's economy as a whole.
In addition, there is no theoretical reason why non-tradable goods and services such as
property costs should be equal in different countries: this is the theoretical reason for PPPs
being different from market exchange rates over time. The relative cost of high-margin products,
such as essential pharmaceutical products, or cellular telephony might compare local capacity
and willingness to pay, as much as relative currency values.
Nevertheless, McDonald's is also using different commercial strategies which can result in huge
differences for a product. Overall, the price of a Big Mac will be a reflection of its local
production and delivery cost, the cost of advertising (considerable in some areas), and most
importantly what the local market will bear – quite different from country to country, and not all a
reflection of relative currency values.
In some markets, a high-volume and low-margin approach makes most sense to maximize
profit, while in others a higher margin will generate more profit. Thus the relative prices reflect
more than currency values. For example, a hamburger costs only €1 in France, and €1.50 in
Belgium, but overall, McDonald's restaurants in both countries cost roughly the same. Prices of
Big Macs can also vary greatly between different areas within a country. For example, a Big Mac
sold in New York City will be more expensive than one sold at a McDonald's located in a rural
area.
One other example is that Russia had one of the cheapest Big Macs at its time in 2019, despite
the fact that Moscow was then the most expensive city in the world. Standard food ingredients
are cheap in Russia, while restaurants suitable for business dinners with English speaking staff
are expensive.
Manipulation

Critics of the presidency of Cristina Fernández de Kirchner in Argentina and many economists
believe that the government has for years falsified consumer price data to understate the
country's true inflation rate. The Economist stated in January 2011 that Big Mac index "does
support claims that Argentina's government is cooking the books. The gap between its average
annual rate of burger inflation (19%) and its official rate (10%) is far bigger than in any other
country." That year the press began reporting on unusual behavior by the more than 200
Argentinean McDonald's restaurants. They no longer prominently advertised Big Macs for sale
and the sandwich, both individually and as part of value meals, was being sold for an unusually
low price compared to other items. Guillermo Moreno, Secretary of Commerce in the Kirchner
government, reportedly forced McDonald's to sell the Big Mac at an artificially low price to
manipulate the country's performance on the Big Mac index. In June 2012, the price of the Big
Mac value meal suddenly rose by 26%, closer to that of other meals, after The Economist, The
New York Times, and other media reported on the unusual pricing. A Buenos Aires newspaper
stated "Moreno loses the battle".
Comparison issues
The Big Mac (and virtually all sandwiches) vary from country to country with differing nutritional
values, weights and even nominal size differences.
Not all Big Mac burgers offered by the chain are exclusively beef. In India – which is a
predominantly Hindu country – beef burgers are not available at any McDonald's outlets. The
Chicken Maharaja Mac serves as a substitute for the Big Mac.
There is a lot of variance with the exclusively beef "Big Mac": the Australian version of the Big
Mac has 22% fewer calories than the Canadian version, and is 8% lighter than the version sold
in Mexico.
On 1 November 2009, all three of the McDonald's in Iceland closed, primarily due to the chain's
high cost of importing most of the chain's meat and vegetables, by McDonald's demands and
standards, from the Eurozone. At the time, a Big Mac in Iceland cost 650 krona ($5.29), and the
20% price increase that would have been needed to stay in business would have increased that
cost to 780 krona ($6.36). Fish and lamb are produced in Iceland, while beef is often imported
(but also exported).
Figures
Six most expensive (July 2023) This statistic shows the most expensive places to buy a Big
Mac.
Switzerland – $7.73 (6.70 CHF)
Norway – $6.92 (70 NOK)
Uruguay – $6.86 (259 UYU)
Argentina – $5.99 (1,650 ARS)
EU – $5.82 (5.28 EUR)
Sweden – $5.74 (60.27 SEK)

Six cheapest (July 2023) This statistic shows the least expensive places to buy a Big Mac.
Taiwan – $2.39 (75 TWD)
Indonesia – $2.52 (38,000 IDR)
India – $2.54 (209 INR)
Egypt – $2.62 (81.00 EGP)
South Africa – $2.81 (49.90 ZAR)
Philippines – $2.82 (155 PHP)
Six fastest earned (July 2015) This statistic shows the average working time required to buy one
Big Mac in selected cities around the world in 2015.
Hong Kong – 8.6 min
Luxembourg – 10.3 min
Japan, Tokyo – 10.4 min
Switzerland, Zürich – 10.6 min
United States, Miami – 10.7 min
Switzerland, Geneva – 10.8 min
Six slowest earned (July 2015) This statistic shows the average working time required to buy
one Big Mac in selected cities around the world in 2015.
Kenya, Nairobi – 172.6 min
Philippines, Manila – 87.5 min
Mexico, Mexico City – 78.4 min
Indonesia, Jakarta – 66.7 min
Egypt, Cairo – 62.5 min
Ukraine, Kyiv – 54.7 min
"""

# Define the system message prompt
systemMessagePrompt = SystemMessagePromptTemplate.from_template(emmo)

# Define the human message prompt
humanMessagePrompt = HumanMessagePromptTemplate.from_template(Paragraph)


chatPrompt = ChatPromptTemplate.from_messages([
    systemMessagePrompt, humanMessagePrompt
])

# Print the generated questions

formattedChatPrompt = chatPrompt.format_messages()

#  try to check error   print("Formatted Chat Prompt:", formattedChatPrompt)

Response = chat.invoke(formattedChatPrompt)
print("Response:", Response)
