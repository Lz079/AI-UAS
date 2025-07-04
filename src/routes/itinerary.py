from flask import Blueprint, request, jsonify
import random

itinerary_bp = Blueprint('itinerary', __name__)

# Sample eco-friendly activities database
ECO_ACTIVITIES = {
    'nature': [
        {
            'name': 'Guided Nature Walk',
            'description': 'Explore local flora and fauna with a certified eco-guide from the community.',
            'duration': '3-4 hours',
            'eco_friendly': True
        },
        {
            'name': 'Organic Farm Visit',
            'description': 'Learn about sustainable farming practices and enjoy farm-to-table meals.',
            'duration': 'Half day',
            'eco_friendly': True
        },
        {
            'name': 'Wildlife Conservation Center',
            'description': 'Support local wildlife conservation efforts and learn about endangered species.',
            'duration': '2-3 hours',
            'eco_friendly': True
        }
    ],
    'cultural': [
        {
            'name': 'Traditional Craft Workshop',
            'description': 'Learn traditional crafts from local artisans and support their livelihood.',
            'duration': '2-3 hours',
            'eco_friendly': True
        },
        {
            'name': 'Community Cultural Center',
            'description': 'Experience authentic cultural performances and interact with locals.',
            'duration': '2 hours',
            'eco_friendly': True
        },
        {
            'name': 'Heritage Walking Tour',
            'description': 'Explore historical sites with local guides who share authentic stories.',
            'duration': '3 hours',
            'eco_friendly': True
        }
    ],
    'food': [
        {
            'name': 'Local Market Tour & Cooking Class',
            'description': 'Shop at local markets and learn to cook traditional dishes with organic ingredients.',
            'duration': '4-5 hours',
            'eco_friendly': True
        },
        {
            'name': 'Farm-to-Table Restaurant',
            'description': 'Dine at restaurants that source ingredients locally and support sustainable practices.',
            'duration': '1-2 hours',
            'eco_friendly': True
        },
        {
            'name': 'Community Food Experience',
            'description': 'Share meals with local families and learn about traditional food culture.',
            'duration': '2-3 hours',
            'eco_friendly': True
        }
    ],
    'adventure': [
        {
            'name': 'Eco-Friendly Hiking Trail',
            'description': 'Hike on designated trails that minimize environmental impact.',
            'duration': '4-6 hours',
            'eco_friendly': True
        },
        {
            'name': 'Sustainable Water Sports',
            'description': 'Enjoy water activities with eco-certified operators who protect marine life.',
            'duration': '3-4 hours',
            'eco_friendly': True
        },
        {
            'name': 'Bicycle Tour',
            'description': 'Explore the area on bicycles, reducing carbon footprint while staying active.',
            'duration': '3-5 hours',
            'eco_friendly': True
        }
    ],
    'relaxation': [
        {
            'name': 'Eco-Spa Experience',
            'description': 'Relax at spas that use natural, locally-sourced products and sustainable practices.',
            'duration': '2-3 hours',
            'eco_friendly': True
        },
        {
            'name': 'Meditation in Nature',
            'description': 'Practice mindfulness in natural settings with minimal environmental impact.',
            'duration': '1-2 hours',
            'eco_friendly': True
        },
        {
            'name': 'Sustainable Beach Activities',
            'description': 'Enjoy beach time while participating in conservation activities like beach cleanups.',
            'duration': '2-4 hours',
            'eco_friendly': True
        }
    ]
}

ACCOMMODATIONS = {
    'budget': [
        'Eco-hostel with solar power and rainwater harvesting',
        'Community-run guesthouse supporting local families',
        'Sustainable backpacker lodge with organic gardens'
    ],
    'mid-range': [
        'Eco-certified boutique hotel with local partnerships',
        'Green hotel with renewable energy and waste reduction',
        'Locally-owned eco-lodge supporting conservation'
    ],
    'luxury': [
        'Luxury eco-resort with carbon-neutral operations',
        'High-end sustainable retreat with community programs',
        'Premium eco-lodge with wildlife conservation initiatives'
    ]
}

COST_RANGES = {
    'budget': {'min': 15, 'max': 50},
    'mid-range': {'min': 30, 'max': 80},
    'luxury': {'min': 60, 'max': 150}
}

def generate_cost(budget_type, activity_type='activity'):
    cost_range = COST_RANGES[budget_type]
    base_cost = random.randint(cost_range['min'], cost_range['max'])
    
    if activity_type == 'accommodation':
        base_cost *= 2  # Accommodation typically costs more
    elif activity_type == 'meal':
        base_cost *= 0.5  # Meals typically cost less
    
    return f"${int(base_cost)}"

def get_activities_by_interests(interests, travel_style):
    """Get activities based on user interests and travel style"""
    activities = []
    
    # Add activities based on travel style
    if travel_style in ECO_ACTIVITIES:
        activities.extend(ECO_ACTIVITIES[travel_style])
    
    # Add activities based on interests
    for interest in interests:
        if interest == 'hiking':
            activities.extend(ECO_ACTIVITIES.get('adventure', []))
        elif interest == 'food':
            activities.extend(ECO_ACTIVITIES.get('food', []))
        elif interest == 'art':
            activities.extend(ECO_ACTIVITIES.get('cultural', []))
        elif interest == 'wildlife':
            activities.extend(ECO_ACTIVITIES.get('nature', []))
        elif interest == 'beaches':
            activities.extend(ECO_ACTIVITIES.get('relaxation', []))
        elif interest == 'markets':
            activities.extend(ECO_ACTIVITIES.get('food', []))
    
    # If no specific activities found, use nature as default
    if not activities:
        activities = ECO_ACTIVITIES['nature']
    
    return activities

@itinerary_bp.route('/generate-itinerary', methods=['POST'])
def generate_itinerary():
    try:
        data = request.get_json()
        
        destination = data.get('destination', 'Unknown Destination')
        duration = data.get('duration', 5)
        budget = data.get('budget', 'mid-range')
        travel_style = data.get('travel_style', 'mixed')
        interests = data.get('interests', [])
        
        # Generate itinerary
        itinerary = []
        available_activities = get_activities_by_interests(interests, travel_style)
        
        for day in range(duration):
            day_activities = []
            
            # Morning activity
            morning_activity = random.choice(available_activities).copy()
            morning_activity['location'] = f"{destination} - Local Area"
            morning_activity['cost'] = generate_cost(budget)
            day_activities.append(morning_activity)
            
            # Lunch
            lunch = {
                'name': 'Local Organic Restaurant',
                'description': 'Enjoy locally-sourced, organic meals at a community-supported restaurant.',
                'location': f"{destination} - City Center",
                'duration': '1 hour',
                'cost': generate_cost(budget, 'meal'),
                'eco_friendly': True
            }
            day_activities.append(lunch)
            
            # Afternoon activity
            afternoon_activity = random.choice(available_activities).copy()
            afternoon_activity['location'] = f"{destination} - Cultural District"
            afternoon_activity['cost'] = generate_cost(budget)
            day_activities.append(afternoon_activity)
            
            # Add accommodation for first day
            if day == 0:
                accommodation = {
                    'name': 'Eco-Friendly Accommodation',
                    'description': random.choice(ACCOMMODATIONS[budget]),
                    'location': f"{destination} - Sustainable District",
                    'duration': f'{duration} nights',
                    'cost': generate_cost(budget, 'accommodation'),
                    'eco_friendly': True
                }
                day_activities.append(accommodation)
            
            day_title = f"Exploring {destination}"
            if day == 0:
                day_title = f"Arrival in {destination}"
            elif day == duration - 1:
                day_title = f"Final Day in {destination}"
            
            itinerary.append({
                'title': day_title,
                'activities': day_activities
            })
        
        return jsonify({
            'success': True,
            'itinerary': itinerary,
            'destination': destination,
            'duration': duration,
            'budget': budget,
            'sustainability_note': 'This itinerary prioritizes eco-friendly activities, local businesses, and sustainable practices to minimize environmental impact while maximizing authentic cultural experiences.'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

