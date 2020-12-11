import import pdb
from models.member import Member 
from models.activity import Activity 
from models.booking import Booking  
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
activity_repository.delete_all()
member_repository.delete_all()

geralt = Member("Geralt", "of Rivia")
ciri = Member("Ciri", "of Cintra")
yennefer = Member("Yennefer", "of Vengerberg")
tris = Member("Tris", "Merigold")

member_repository.save(geralt)
member_repository.save(ciri)
member_repository.save(yennefer)
member_repository.save(tris)

emotions = Activity("Emotions Yoga", "hollistic", False)
sword = Activity("Sword Fighting", "essentials", False)
spells = Activity("Spells", "magic", False)

activity_repository.save(emotions)
activity_repository.save(sword)
activity_repository.save(spells)

booking_1 = Booking(geralt, emotions)
booking_2 = Booking(ciri, sword)
booking_3 = Booking(yennefer, spells)
booking_4 = Booking(tris, spells)
booking_5 = Booking(ciri, spells)