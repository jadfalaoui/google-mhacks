from django.shortcuts import render
import pathlib
import textwrap
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

# Create your views here.

GOOGLE_API_KEY= "AIzaSyAoaSv_0V1dxXfkdorC10rKbH3R5i68Fmw"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(
    'gemini-pro',
    generation_config=genai.GenerationConfig(
        max_output_tokens=10000,
        temperature=0.9,
    ))

def blackbox(data):
   location = "Orlando, Florida" #str(input("Location?\n"))
    age = data["age"]
    budget = "500"#str(input("Budget? (Per person)\n"))
    accompanied = data["groupSize"]
    numberDays = "6"#str(input("Number of days?\n"))
    activity = "Exciting"#str(input("How active would you like to be?\n"))
    numPeople = data["groupSize"]#str(input("Number of people?\n"))
    additionalCom = "Want to go skydiving"#str(input("Additional comments?\n"))
    response = model.generate_content('Imagine you were a tour guide that is an expert at planning ' + activity + ' active trips. ' +'Search highly rated activities in the area and give a specific itenerary for a traveler that is ' + age + 
    ' years old and wants to go to ' + location + ' with ' + budget + 'dollars per person with ' + numPeople + 
    ' people, all of whom are their' + accompanied + ' and for ' + numberDays + ' days. Additional comments are: '+ additionalCom + '. Each day should be split into 3 different sections: Morning, Noon, and Night. Each section must include a meal **MANDATORY (breakfast for monring, lunch for noon, dinner for evening).\n\n' + 
    'Give it in this EXACT (DO NOT CHANGE THE FORMAT OR INCLUDE ANY STARS OR ASTERICKS Do not output **Day 6:**\n**Morning:** and instead output Day6:\nMoning:\n Do not include any punctuation except for colons, parentheses, and dollar signs): ' +
    'For example, if given the input of location: Spain, age: 15, budget: 1500, number of days: 5, activity: Spunky, accompanied by: family and number of people: 5 with no additional comments, output exactly for Day 1: "Day 1:\nMorning:\nBreakfast at Chocolatería San Ginés $10-20 (Traditional Spanish breakfast spot with churros and chocolate)\nVisit the Royal Palace of Madrid ' +
    '(Explore the grandeur of the Spanish monarchy)\nNoon:\nLunch at Botín $15-30 (Worlds oldest restaurant, serving traditional Spanish cuisine)\nWalk through El Retiro Park (Relax and explore the beautiful gardens)\nNight:\n' +
    'Attend a Flamenco show at Tablao Cordobes $40-60 (Experience the vibrant and passionate dance form)\nDinner at Casa Lucio $30-50 (Michelin-starred restaurant known for its traditional Spanish dishes)\n" If given the input Africa, age: 15, budget: 1500, number of days: 5, activity: Spunky, accompanied by: Friends and number of people: 5, output exactly for Day 5' +
    'Day 5:\n' +
    'Morning:\n' +
    'Breakfast at the Kempinski Hotel Gold Coast City $10-20 (Indulge in a luxurious breakfast with a serene ambiance)\n' +
    'Visit the W.E.B. Du Bois Centre $5 (Explore the life and legacy of the renowned Pan-Africanist)\n' +
    'Noon:\n' +
    'Lunch at Coco Beach $15-30 (Relish a delightful lunch while enjoying the scenic beach views)\n' +
    'Visit the Labadi Beach $3 per person (Unwind and swim in the refreshing Atlantic Ocean)\n' +
    'Night:\n' +
    'Farewell dinner at The Capital Kitchen $30-50 (Conclude your trip with a memorable dining experience in a stylish and sophisticated setting)\n' +
    'If given the location: Puerto Rico, age: 25, budget: 800, number of days: 10, activity: Fun, accompanied by: Friends and number of people: 10, output exactly for the consecutive days 6 and 7:'
    'Day 6:\nMorning:\nBreakfast at Abracadabra Coffee Roasters $10-20 (Artisanal coffee and specialty breakfast sandwiches)\nVisit the Castillo San Felipe del Morro $15-30 (Explore the historic Spanish fort)\nNoon:\nLunch at El Alambique $15-30 (Traditional Puerto Rican cuisine with a cozy atmosphere)' +
    '\nShop for local souvenirs and crafts at the Plaza de Colón\nNight:\nGo stargazing at the Puerto Rico Observatory $20-30 (Observe the night sky through telescopes and learn about astronomy)\nDinner at El Platanal $30-50 (Contemporary Puerto Rican cuisine with a focus on local ingredients)' +
    '\nDay 7:\nMorning:\nBreakfast at Happy Cafe $10-20 (Casual breakfast spot with a variety of options)\nVisit the Bioluminescent Bay in Fajardo $40-60 (Experience the magical glow of bioluminescent plankton)\nNoon:\nLunch at La Casa Del Frances $15-30 (Seafood restaurant with a beautiful beachfront view)' +
    '\nRelax on Seven Seas Beach (Enjoy the white sand beaches and crystal-clear waters)\nNight:\nHave a bonfire on the beach $10-20 (Gather around a roaring fire and roast marshmallows)\nDinner at Marbella $30-50 (Seafood restaurant with a romantic ambiance)'+
    '\nHere is a complete example (follow exactly) of an output given the input location: Japan, age: 70, budget: 2000, number of days: 6, activity: Relaxing, and number of people: 5\n' 
    '''Day 1:
    Morning:
    Breakfast at Kagurazaka Cafe $5 (Savor a traditional Japanese breakfast in a quaint cafe)
    Visit the Tokyo National Museum $5 (Explore Japans rich history and art)
    Noon:
    Lunch at Tenmatsu $10 (Indulge in authentic sushi at a renowned restaurant)
    Shop for souvenirs at Nakamise Street (Discover a vibrant shopping street filled with traditional Japanese goods)
    Night:
    Attend a Kabuki theater performance $20 (Witness the captivating artistry of traditional Japanese theater)
    Dinner at Ginza Kyubey $30 (Experience the exquisite flavors of traditional Japanese cuisine)
    Day 2:
    Morning:
    Breakfast at Bills Tokyo $10 (Enjoy a delightful breakfast with stunning city views)
    Visit the Tsukiji Fish Market $15 (Witness the bustling atmosphere and fresh seafood)
    Noon:
    Lunch at Sushi Dai $20 (Savor fresh and innovative sushi at a Michelin-starred restaurant)
    Visit the Tokyo Skytree $25 (Ascend to the citys tallest tower for panoramic views)
    Night:
    Stroll through the Akihabara district $10 (Explore Japans renowned electronics and anime hub)
    Dinner at Gonpachi Nishi-Azabu $35 (Dine in the iconic setting featured in the film "Kill Bill")
    Day 3:
    Morning:
    Breakfast at Amanoya $15 (Indulge in a traditional Japanese breakfast in a serene teahouse)
    Visit the Ghibli Museum $20 (Immerse yourself in the magical world of Studio Ghiblis animations)
    Noon:
    Lunch at Jiro Ono $50 (Experience the legendary omakase sushi experience)
    Visit Meiji Jingu Shrine $5 (Explore the peaceful and serene surroundings of a Shinto shrine)
    Night:
    Attend a Noh theater performance $30 (Witness the ancient and refined art form of Japanese theater)
    Dinner at Joël Robuchon $75 (Celebrate with an unforgettable fine dining experience)
    Day 4:
    Morning:
    Breakfast at Pierre Hermé Paris $15 (Savor delectable pastries and coffee in a luxurious setting)
    Visit the Tokyo Imperial Palace $10 (Explore the historic grounds and gardens)
    Noon:
    Lunch at Tempura Kondo $25 (Enjoy crispy and flavorful tempura at a renowned restaurant)
    Visit the Kabuki-za Theater $30 (Admire the traditional architecture and catch a performance)
    Night:
    Attend a traditional tea ceremony $20 (Experience the tranquility and elegance of Japanese tea culture)
    Dinner at Zauo Shinjuku $35 (Participate in a unique fishing experience and enjoy fresh seafood)
    Day 5:
    Morning:
    Breakfast at Yanaka Coffee $10 (Indulge in aromatic coffee and pastries in a cozy cafe)
    Visit the Nezu Shrine $5 (Explore a beautiful and peaceful garden sanctuary)
    Noon:
    Lunch at Taito $15 (Savor delicious and affordable ramen in a lively atmosphere)
    Visit the Asakusa district $10 (Discover traditional Japanese culture and architecture)
    Night:
    Stroll through the Shinjuku Gyoen National Garden $10 (Admire stunning landscapes and seasonal flowers)
    Dinner at Teppanyaki Ginza Onodera $60 (Witness the culinary artistry of teppanyaki cuisine)
    Day 6:
    Morning:
    Breakfast at Ginza Cozy Corner $5 (Delight in Japanese pastries and coffee in a convenient location)
    Visit the Mori Art Museum $20 (Explore contemporary and modern art exhibitions)
    Noon:
    Lunch at Tonkatsu Maisen $20 (Indulge in crispy and juicy tonkatsu at a famous restaurant)
    Visit the Harajuku district $10 (Experience the vibrant and eclectic fashion and youth culture)
    Night:
    Attend a karaoke session $20 (Sing your heart out in a private karaoke room)
    Dinner at Ichiran $15 (Savor authentic tonkotsu ramen in a unique setting)\n\n'''
    '''If given the input location: Orlando, Florida, age: 20, budget: 500, number of days: 6, activity: Exciting, and number of people: 5 with the additional comment "Want to go skydiving", output:
    Day 1:
    Morning:
    Breakfast at Keke's Breakfast Cafe: $10-15 (Indulge in classic American breakfast dishes)
    Visit ICON Park: $60-70 (Thrilling amusement park with The Wheel, Madame Tussauds, and Sea Life)
    Noon:
    Lunch at Bosphorous Turkish Cuisine: $15-25 (Authentic Turkish cuisine with a lively ambiance)
    Explore Lake Eola Park: $0 (Tranquil park with a scenic lake, swans, and gardens)
    Night:
    Attend a performance at Dr. Phillips Center for the Performing Arts: $20-40 (World-renowned performing arts center)
    Dinner at The Ravenous Pig: $30-40 (Upscale gastropub with a modern American menu)
    Day 2:
    Morning:
    Breakfast at The Earthy Kitchen: $10-15 (Wholesome and organic breakfast options)
    Visit Kennedy Space Center: $50-60 (Immersive space exploration experience with exhibits and attractions)
    Noon:
    Lunch at Dixie Crossroads: $15-25 (Classic Southern comfort food in a cozy setting)
    Shop at the Florida Mall: $0 (Extensive shopping mall with various retail stores and dining options)
    Night:
    Go skydiving at Skydive Space Center: $250-300 (Adrenaline-pumping skydiving experience)
    Dinner at Morimoto Asia: $35-45 (Modern Asian cuisine with a sophisticated ambiance)
    Day 3:
    Morning:
    Breakfast at Se7en Bites: $10-15 (Creative and flavorful breakfast options)
    Visit the Harry Potter™ world at Universal Orlando Resort: $100-120 (Immersive experience into the magical world of Harry Potter)
    Noon:
    Lunch at Three Broomsticks: $15-25 (Authentic Harry Potter-themed dining experience)
    Explore CityWalk: $0 (Vibrant entertainment complex with restaurants, shops, and attractions)
    Night:
    Attend a concert at House of Blues: $30-50 (Live music venue with a lively atmosphere)
    Dinner at The Boathouse: $35-45 (Seafood restaurant with waterfront views)
    Morning:
    Breakfast at Broken Egg Cafe: $10-15 (Comfortable breakfast spot with a wide menu)
    Visit the Central Florida Zoo & Botanical Gardens: $25-35 (Diverse zoological and botanical attractions)
    Noon:
    Lunch at The Thirsty Topher: $15-25 (Lively Irish pub with traditional fare)
    Rent a boat and explore Lake Ivanhoe: $50-70 (Enjoy a scenic boat ride and take in the lake's beauty)
    Night:
    Have dinner at Prato: $35-45 (Contemporary Italian restaurant with a sophisticated ambiance)
    Attend a magic show at Sleight of Hand Society: $30-40 (Intimate magic show with skilled performers)
    Day 5:
    Morning:
    Breakfast at Winter Park Biscuit Company: $10-15 (Casual breakfast spot with a variety of biscuit-based dishes)
    Visit the Charles Hosmer Morse Museum of American Art: $12-15 (Impressive collection of Louis Comfort Tiffany's stained glass and decorative arts)
    Noon:
    Lunch at The Ravenous Pig Winter Park: $15-25 (Upscale gastropub with a modern American menu)
    Shop at Park Avenue: $0 (Charming shopping and dining district with boutiques, art galleries, and restaurants)
    Night:
    Attend a play at the Orlando Shakespeare Theater: $20-30 (Renowned theater company with a variety of productions)
    Dinner at The Courtesy Bar: $35-45 (Hip and trendy cocktail bar with a creative menu)
    Day 6:
    Morning:
    Breakfast at Hash House A Go Go: $10-15 (Quirky breakfast spot with over-the-top dishes)
    Visit the Legoland Florida Resort: $80-100 (Interactive theme park based on the popular Lego brand)
    Noon:
    Lunch at Fun Town Pizza: $15-25 (Family-friendly pizza restaurant with arcade games)
    Explore Pirate's Cove Adventure Golf: $15-20 (Miniature golf course with a pirate-themed atmosphere)
    Night:
    Attend a stand-up comedy show at The Improv: $20-30 (Renowned comedy club with regular performances)
    Dinner at Rocco's Tacos: $15-25 (Vibrant Mexican restaurant with authentic flavors)
    '''
    'Use up the majority of the budget. Activities should be specific locations and should not be vague. For example, do not output "Go stargazing $20-30" and instead state the location "Go stargazing at the Puerto Rico Observatory $20-30. Keep all monetary values in dollars (Dont output Breakfast at Kagurazaka Cafe 730yen and instead output Breakfast at Kagurazaka Cafe $5)')
return response.text

def index(request):
    context = {}
    return render(request,'index.html')

class AIAPIView(APIView):
    def post(self, request, *args, **kwargs):
        input_data = request.data
        print(input_data)
        result = blackbox(input_data)
        return Response(result, status=status.HTTP_200_OK)
    






responseText = response.text
endText = responseText.split('\n')



print(endText)