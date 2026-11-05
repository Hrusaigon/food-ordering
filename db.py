import sqlite3

db = sqlite3.connect("food.db")
cursor = db.cursor()

QUERY = '''
            create table if not exists category(
                id INTEGER primary key autoincrement,
                category char(36)
            )
        '''
db.commit()
cursor.execute(QUERY)

QUERY = '''
            create table if not exists menu(
                id INTEGER primary key autoincrement,
                category_id integer,
                name char(36),
                description text,
                price char(10),
                image text,
                FOREIGN KEY (category_id) REFERENCES category(id)
            )
        '''

db.commit()
cursor.execute(QUERY)

data = [
    ("Appetizers",),
    ("Mains",),
    ("Desserts",),
    ("Drinks",)
]

cursor.executemany("""
    INSERT INTO category (category)
    VALUES (?)
""", data)
db.commit()

data = [
    # Appetizers (category_id = 1)
    (
        1,
        "Bread & dips",
        "Sourdough bread accompanied by hummus, beetroot & whipped feta dips",
        "https://i.pinimg.com/736x/7f/ca/9f/7fca9f2965885a06091ec85c44a745c7.jpg",
        "£4.50"
    ),
    (
        1,
        "Green salad - Small",
        "A garden-fresh salad with seasonal greens and roasted almonds",
        "https://i.pinimg.com/1200x/f4/88/92/f4889253c3756aa1ab66f45cf23108fb.jpg",
        "£3.50"
    ),
    (
        1,
        "Green salad - Medium",
        "A garden-fresh salad with seasonal greens and roasted almonds",
        "https://i.pinimg.com/1200x/f4/88/92/f4889253c3756aa1ab66f45cf23108fb.jpg",
        "£5.50"
    ),
    (
        1,
        "Tuna sashimi",
        "Seared fresh tuna, fresh herbs, and a touch of chili",
        "https://i.pinimg.com/1200x/ae/52/54/ae525424ffe6c7abac97f0c7e241b0a0.jpg",
        "£4.50"
    ),

    # Mains (category_id = 2)
    (
        2,
        "Hand-made ravioli",
        "Artisanal hand-made ravioli, filled with a blend of cheeses in a basil pesto sauce",
        "https://i.pinimg.com/736x/09/40/b1/0940b10ff5bdc337717dfd2198bc8410.jpg",
        "£6.50"
    ),
    (
        2,
        "Tofu skewers",
        "Grilled tofu skewers, marinated in a blend of soy and sesame with seasonal roast vegetables",
        "https://i.pinimg.com/1200x/04/49/5a/04495a3a134f39dc1fc45450c22bd56d.jpg",
        "£7.50"
    ),
    (
        2,
        "Fish of the day",
        "Fresh catch of the day paired with asparagus & a cream of sweet potato",
        "https://i.pinimg.com/1200x/5e/34/2f/5e342fbed121b11ecba64fe0d72d3700.jpg",
        "£8.00"
    ),
    (
        2,
        "Peanut crusted steak",
        "Juicy, tender steak cooked to your liking, served with steamed vegetables",
        "https://i.pinimg.com/1200x/bc/31/13/bc311320eec6f465f632971c3bc58974.jpg",
        "£8.00"
    ),
    (
        2,
        "Classic burger - Mushroom",
        "Our classic burger with lettuce, pickles, heirloom tomatoes, served with a side of fries",
        "https://i.pinimg.com/736x/a6/cd/18/a6cd181ac7bdca461d7ce9d0e0ed0454.jpg",
        "£7.00"
    ),
    (
        2,
        "Classic burger - Chicken",
        "Our classic burger with lettuce, pickles, heirloom tomatoes, served with a side of fries",
        "https://i.pinimg.com/736x/a6/cd/18/a6cd181ac7bdca461d7ce9d0e0ed0454.jpg",
        "£7.50"
    ),
    (
        2,
        "Classic burger - Beef",
        "Our classic burger with lettuce, pickles, heirloom tomatoes, served with a side of fries",
        "https://i.pinimg.com/736x/a6/cd/18/a6cd181ac7bdca461d7ce9d0e0ed0454.jpg",
        "£9.00"
    ),
    (
        2,
        "Schnitzel",
        "Crisp and golden on the outside, in a herb and parmesan crumb",
        "https://i.pinimg.com/1200x/71/6e/f0/716ef044f3c9ca9ad7115b57af8f2ce5.jpg",
        "£4.00"
    ),

    # Desserts (category_id = 3)
    (
        3,
        "Sticky date & ice cream",
        "Served with vanilla ice cream, toffee sauce & a peanut crumble",
        "https://i.pinimg.com/1200x/96/7e/07/967e078c55f309aa756b0d79ae5b3dff.jpg",
        "£7.00"
    ),
    (
        3,
        "Classic cheesecake",
        "Topped with a layer of raspberry jam & sliced strawberries",
        "https://i.pinimg.com/1200x/96/7e/07/967e078c55f309aa756b0d79ae5b3dff.jpg",
        "£6.50"
    ),
    (
        3,
        "Lemon meringue pie",
        "Zesty lemon meringue, a pistachio crumble, served with a chantilly cream",
        "https://halicopteraway.com/wp-content/uploads/2023/02/IMG_0052-2-819x1024.jpg",
        "£5.50"
    ),
    (
        3,
        "Chocolate mousse - Single serve",
        "Our delicate, yet rich signature chocolate mousse dessert",
        "https://i.pinimg.com/736x/87/99/00/879900751c203956fd37ed87f1113e17.jpg",
        "£4.00"
    ),
    (
        3,
        "Chocolate mousse - Double serve",
        "Our delicate, yet rich signature chocolate mousse dessert",
        "https://i.pinimg.com/736x/87/99/00/879900751c203956fd37ed87f1113e17.jpg",
        "£7.00"
    ),
    (
        3,
        "Carrot cake",
        "Lightly spiced carrot cake layered with cream cheese frosting",
        "https://i.pinimg.com/1200x/be/75/96/be7596618eff0aa13e28fff4617028dc.jpg",
        "£5.50"
    ),
    (
        3,
        "Brownie",
        "Fresh out the oven brownie filled with dark chocolate chips & walnuts",
        "https://i.pinimg.com/736x/72/7c/45/727c456547c2dd6df23a012e50d9f310.jpg",
        "£5.00"
    ),

    # Drinks (category_id = 4)
    (
        4,
        "Healthy smoothie",
        "Nourish your body with our selection of healthy smoothies",
        "https://i.pinimg.com/736x/27/0b/8c/270b8c2f823c9e297332686fc465e90e.jpg",
        "£3.00"
    ),
    (
        4,
        "Fresh juice - Small",
        "A refreshing blend of freshly squeezed orange, watermelon, carrot, and ginger",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNKXalhm_aMlQDgYfYOQ8dx-FlBtb4Z1ObmRIvFkGiDQ&s=10",
        "£2.00"
    ),
    (
        4,
        "Fresh juice - Medium",
        "A refreshing blend of freshly squeezed orange, watermelon, carrot, and ginger",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNKXalhm_aMlQDgYfYOQ8dx-FlBtb4Z1ObmRIvFkGiDQ&s=10",
        "£3.00"
    ),
    (
        4,
        "Fresh juice - Large",
        "A refreshing blend of freshly squeezed orange, watermelon, carrot, and ginger",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNKXalhm_aMlQDgYfYOQ8dx-FlBtb4Z1ObmRIvFkGiDQ&s=10",
        "£4.00"
    ),
    (
        4,
        "Wine",
        "Choice of red, white, or rosé",
        "https://i.pinimg.com/736x/ae/16/d6/ae16d6d9323a44d84a59384e66961bd8.jpg",
        "£2.00"
    ),
    (
        4,
        "Soft drink",
        "Soda, Sprite, Pepsi & Diet Coke",
        "https://i.pinimg.com/736x/79/6c/34/796c34906c9111f02f41a319298a261b.jpg",
        "£1.50"
    ),
    (
        4,
        "Coffee",
        "Locally roasted coffee, brewed in-house",
        "https://i.pinimg.com/736x/21/74/32/2174329b8ef1603c1cbc68bd9ef5865a.jpg",
        "£2.50"
    ),
    (
        4,
        "Cocktails",
        "Aperol Spritz, Gin & Tonic, Mojito",
        "https://i.pinimg.com/1200x/8d/c9/68/8dc968f43b13b8e13a4a24a42ee73203.jpg",
        "£1.50"
    )
]

cursor.executemany("""
    INSERT INTO menu (category_id, name, description, image, price)
    VALUES (?, ?, ?, ?, ?)
""", data)
db.commit()