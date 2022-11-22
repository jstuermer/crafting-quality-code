"""
A restaurant recommendation system.

Here are some example dictionaries that correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{
    "Georgie Porgie": 87,
    "Queen St. Cafe": 82,
    "Dumplings R Us": 71,
    "Mexican Grill": 85,
    "Deep Fried Everything": 52
}

Price to list of restaurant names:
# dict of {str: list of str}
{
    "$": ["Queen St. Cafe", "Dumplings R Us", "Deep Fried Everything"],
    "$$": ["Mexican Grill",],
    "$$$": ["Georgie Porgie"],
    "$$$$": []
}

Cuisine to list of restaurant names:
# dict of {str: list of str}
{
    "Canadian": ["Georgie Porgie"],
    "Pub Food": ["Georgie Porgie", "Deep Fried Everything"],
    "Malaysian": ["Queen St. Cafe"],
    "Thai": ["Queen St. Cafe"],
    "Chinese": ["Dumplings R Us"],
    "Mexican": ["Mexican Grill"]
}

Given this data, a price of "$" and a list of cuisines like ["Chinese", "Thai"],
we would produce the following list, which is sorted according to the ratings:

    [[82, "Queen St. Cafe"], [71, "Dumplings R Us"]]
"""

# The file containing the restaurant data
FILENAME = "restaurants_small.txt"

def recommend(file, price, cuisines_list):
    """
    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisine_list. Return a list of lists of the
    form [rating%, restaurant name], sorted by rating%.

    Parameters
    ----------
    file : str
        The input file containing the restaurant information.
    price : str
        The desired price.
    cuisines_list : list
        The desired cuisines.

    Returns
    -------
    list of [int, str] lists
        A list of lists of the form [rating%, restaurant name], sorted by
        rating%. Each entry represents a viable restaurant.
    """

    # Read the file and build the required data structures
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    # Get the list of restaurant names for the requested price
    names_matching_price = price_to_names[price]

    # Filter out the restaurants that do not serve the desired cuisine
    names_matching = filter_by_cuisine(
        names_matching_price,
        cuisine_to_names,
        cuisines_list
    )

    # Sort the restaurant list according to the ratings
    rating_list = build_rating_list(name_to_rating, names_matching)
    return rating_list

def build_rating_list(name_to_rating, restaurant_names):
    """
    Returns a sorted list of lists of the form [rating%, restaurant name]
    starting with the highest-rated restaurant in restaurant_names.

    Parameters
    ----------
    name_to_rating : dict of {str: int}
        Dictionary containing the ratings of restaurants.
    restaurant_names : list of str
        A list of restaurant names which are to be sorted according to their
        rating.

    Returns
    -------
    list of [int, str] lists
        The restaurant ratings and names sorted according to the ratings.

    Examples
    --------
    >>> name_to_rating = {
        "Georgie Porgie": 87,
        "Queen St. Cafe": 82,
        "Dumplings R Us": 71,
        "Mexican Grill": 85,
        "Deep Fried Everything": 52
    }
    >>> names = ["Queen St. Cafe", "Dumplings R Us"]
    >>> build_rating_list(name_to_rating, names)
    [[82, "Queen St. Cafe"], [71, "Dumplings R Us"]]
    """

    rating_list = [[name_to_rating[name], name] for name in restaurant_names]
    rating_list.sort()
    rating_list.reverse()

    return rating_list

def filter_by_cuisine(restaurant_names, cuisine_to_names, cuisines_list):
    """
    Returns a list of all restaurants in restaurant_names that serve any of the
    cuisines in cuisines_list.

    Parameters
    ----------
    restaurant_names : list of str
        The restaurants to be filtered by cuisine.
    cuisine_to_names : dict of {str: list of str}
        Dictionary defining which cuisine is served by which restaurants.
    cuisines_list : list of str
        The desired cuisines.

    Returns
    -------
    list of str
        The list of restaurants serving any of the cuisines in cuisines_list.

    Examples
    --------
    >>> names = ["Queen St. Cafe", "Dumplings R Us", "Deep Fried Everything"]
    >>> cuisine_to_names = {
        "Canadian": ["Georgie Porgie"],
        "Pub Food": ["Georgie Porgie", "Deep Fried Everything"],
        "Malaysian": ["Queen St. Cafe"],
        "Thai": ["Queen St. Cafe"],
        "Chinese": ["Dumplings R Us"],
        "Mexican": ["Mexican Grill"]
    }
    >>> cuisines_list = ["Chinese", "Thai"]
    >>> filter_by_cuisine(names, cuisine_to_names, cuisines_list)
    ["Queen St. Cafe", "Dumplings R Us"]
    """

    restaurants_filtered = []
    for name in restaurant_names:
        cuisines_served = [
            c for c in cuisine_to_names if name in cuisine_to_names[c]
        ]
        if any(c in cuisines_list for c in cuisines_served):
            restaurants_filtered.append(name)

    return restaurants_filtered

def read_restaurants(file):
    """
    Extract important information on restaurants from file.

    Parameters
    ----------
    file : str
        The input file containing the restaurant information.

    Returns
    -------
    (dict, dict, dict)
        The following specific information on the restaurants:

        - a dict of {restaurant name: rating%}
        - a dict of {price: list of restaurant names}
        - a dict of {cuisine: list of restaurant names}
    """

    name_to_rating = {}
    price_to_names = {"$": [], "$$": [], "$$$": [], "$$$$": []}
    cuisine_to_names = {}

    props_per_restaurant = 4 # number of properties per restaurant

    # Get restaurant properties from file
    props = get_props(file)

    n_restaurants = len(props) // props_per_restaurant
    for i in range(0, n_restaurants):
        # Get properties of current restaurant
        start = i * props_per_restaurant # first property of current restaurant
        name = props[start]
        rating = props[start+1][0:-1] # excluding the % symbol
        price = props[start+2]
        cuisines = props[start+3].split(",")

        # Add properties to dictionaries
        name_to_rating[name] = rating
        price_to_names[price].append(name)
        for c in cuisines:
            if c not in cuisine_to_names:
                cuisine_to_names[c] = [name]
            else:
                cuisine_to_names[c].append(name)

    return name_to_rating, price_to_names, cuisine_to_names

def get_props(file):
    """
    Extract restaurant properties from file while excluding empty lines and line
    breaks.

    Parameters
    ----------
    file : str
        The input file containing the restaurant information.

    Returns
    -------
    list
        A list of all restaurant properties in file.
    """

    props = []
    with open(file) as f:
        lines = f.readlines()
        props = [p.strip() for p in filter(lambda l: len(l.strip()) > 0, lines)]

    return props