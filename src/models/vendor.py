from sqlalchemy import Column, Integer, String, ForeignKey, Boolean,Text,BigInteger
from sqlalchemy.orm import relationship,Mapped
from ..database import Base

class VendorModel(Base):
    __tablename__ = "vendor"

    name = Column(String(50))
    Phone = Column(BigInteger)
    institute=Column(String(50))
    email = Column(String(50),nullable=False,primary_key=True)
    Address_line_1=Column(String(50))
    Address_line_2=Column(String(50))
    City=Column(String(50))
    State=Column(String(50))
    Pincode=Column(BigInteger)
    Country=Column(String(50))
    mess_name=Column(String(50))
    isapproved = Column(Boolean)
    type= Column(String(50))
    status=Column(Boolean)
    starttime=Column(String(50))
    endtime=Column(String(50))




class DeletedVendorModel(Base):
    __tablename__ = "deleted_vendors"

    name = Column(String(50))
    Phone = Column(BigInteger)
    institute=Column(String(50))
    email = Column(String(50),nullable=False,primary_key=True)
    Address_line_1=Column(String(50))
    Address_line_2=Column(String(50))
    City=Column(String(50))
    State=Column(String(50))
    Pincode=Column(BigInteger)
    Country=Column(String(50))
    mess_name=Column(String(50))
    isapproved = Column(Boolean)

class MenuModel(Base):
    __tablename__ = "menu"
    id = Column(BigInteger, primary_key=True,index=True)
    user_id = Column(String(50),nullable=False) 
    breakfast = Column(String(50))
    lunch = Column(String(50))
    snacks = Column(String(50))
    dinner = Column(BigInteger)
    date = Column(String(50))
    institute=Column(String(50))
    calories_breakfast=Column(String(50))
    calories_lunch=Column(String(50))
    calories_snacks=Column(String(50))
    calories_dinner=Column(String(50))
    mess_name=Column(String(50))



class InternalVendorMenuModel(Base):
    __tablename__ = "internalvendormenu"
    id = Column(BigInteger, primary_key=True,index=True)
    user_id = Column(String,nullable=False) 
    menu=Column(String(50))
    price=Column(String(50))
    institute=Column(String(50))
    mess_name=Column(String(50))
    
    
    

class SessionModel(Base):
    __tablename__="session"
    
    sessionId = Column(Text(), primary_key=True)
    email = Column(String(50))

class CancelledOrders(Base):
    __tablename__="cancelled_orders"
    id = Column(BigInteger,index=True, primary_key=True)
    email_of_consumer=Column(String(50))
    name_of_consumer=Column(String(50))
    vendor_email=Column(String(50))
    Address_line_1 = Column(String(50))
    Address_line_2 = Column(String(50))
    Phone = Column(BigInteger)
    date = Column(String(50))
    institute= Column(String(50))
    items=Column(String(50))
    quantities=Column(String(50))
    prices=Column(String(50))
    outlet_name=Column(String(50))

class DeliveredOrders(Base):
    __tablename__="delivered_orders"
    id = Column(BigInteger,index=True, primary_key=True)
    email_of_consumer=Column(String(50))
    name_of_consumer=Column(String(50))
    vendor_email=Column(String(50))
    Address_line_1 = Column(String(50))
    Address_line_2 = Column(String(50))
    Phone = Column(BigInteger)
    date = Column(String(50))
    institute= Column(String(50))
    items=Column(String(50))
    quantities=Column(String(50))
    prices=Column(String(50))
    outlet_name=Column(String(50))

class CalorieTracker(Base):
    __tablename__="calorie_info"
    id = Column(BigInteger,index=True, primary_key=True)
    items=Column(String(50))
    calories=Column(String(50)) 



