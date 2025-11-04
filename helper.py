from faker import Faker

faker = Faker()

def generate_registration_data():
    name = faker.name()
    telegram_nick = faker.nickname()
    phone = faker.phone_number()
    additional_info = faker.email()
    return name, telegram_nick, phone, additional_info