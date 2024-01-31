from jeju import db

class selectData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.INT, nullable=False)
    month_str= db.Column(db.String(200), nullable=False)
    spot1 = db.Column(db.INT, nullable=False)
    spot1_str= db.Column(db.String(200), nullable=False)
    spot2 = db.Column(db.INT, nullable=False)
    spot2_str= db.Column(db.String(200), nullable=False)
    food = db.Column(db.INT, nullable=False)
    food_str= db.Column(db.String(200), nullable=False)
    pet = db.Column(db.INT, nullable=False)
    pet_str = db.Column(db.String(200), nullable=False)
    pool = db.Column(db.INT, nullable=False)
    garden = db.Column(db.INT, nullable=False)
    sea = db.Column(db.INT, nullable=False)
    nocost = db.Column(db.INT, nullable=False)
    bus = db.Column(db.INT, nullable=False)
    police = db.Column(db.INT, nullable=False)
    hospital = db.Column(db.INT, nullable=False)
    bank = db.Column(db.INT, nullable=False)
    mart = db.Column(db.INT, nullable=False)
    gift = db.Column(db.INT, nullable=False)


class Pension(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    reviewNum = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    pension_keyword = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    ammen = db.Column(db.String(200), nullable=False)
    pensionID = db.Column(db.Integer, nullable=False)
    ammen1 = db.Column(db.String(200), nullable=False)
    ammen2 = db.Column(db.String(200), nullable=False)
    ammen3 = db.Column(db.String(200), nullable=False)
    ammen4 = db.Column(db.String(200), nullable=False)
    ammen5 = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)


class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)
    sat = db.Column(db.Integer, nullable=False)
    sun = db.Column(db.Integer, nullable=False)
    holiday = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)

class Police(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    homepage = db.Column(db.String(200), nullable=False)

class Parm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)

class Mart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)

class Bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)

class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=True)
    review_rating = db.Column(db.Float, nullable=True)
    review = db.Column(db.String(200), nullable=True)
    homepage = db.Column(db.String(200), nullable=True)

class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)
    detailtype = db.Column(db.String(200), nullable=False)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)
    detailtype = db.Column(db.Integer, nullable=False)
    detailtype_str = db.Column(db.String(200), nullable=False)
    detailtype2_str = db.Column(db.String(200), nullable=False)

class Olleh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    course_name= db.Column(db.String(200), nullable=False)
    distance = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.String(200), nullable=False)
    start_point = db.Column(db.String(200), nullable=False)
    end_pointt = db.Column(db.String(200), nullable=False)

class Weather_point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    point = db.Column(db.String(200), nullable=False)

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(200), nullable=False)
    point = db.Column(db.Integer, nullable=False)
    point_name = db.Column(db.String(200), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    rain = db.Column(db.Float, nullable=False)
    wind = db.Column(db.Float, nullable=False)
    sun = db.Column(db.Float, nullable=False)
    snow = db.Column(db.Float, nullable=False)
    ground = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)

class Pm_point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(200), nullable=False)


class Pm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(200), nullable=False)
    강정동 = db.Column(db.Float, nullable=False)
    남원읍 = db.Column(db.Float, nullable=False)
    대정읍 = db.Column(db.Float, nullable=False)
    동홍동 = db.Column(db.Float, nullable=False)
    성산읍 = db.Column(db.Float, nullable=False)
    애월읍 = db.Column(db.Float, nullable=False)
    연동 = db.Column(db.Float, nullable=False)
    이도동 = db.Column(db.Float, nullable=False)
    조천읍 = db.Column(db.Float, nullable=False)
    한림읍 = db.Column(db.Float, nullable=False)
    화북동 = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)













