from . import db

class Patient(db.Model):
    __tablename__ = 'patient'
    patientID = db.Column(db.CHAR(4), primary_key=True)  # 每个用户记得添加用户组
    name = db.Column(db.CHAR(20))
    gender = db.Column(db.CHAR(1))
    birthDay = db.Column(db.DATE)
    phoneNumber = db.Column(db.CHAR(11))
    address = db.Column(db.CHAR(20))
    password = db.Column(db.VARCHAR(100))

    reservationrefer = db.relationship('Reservation', backref='patient')
    prescriptionrefer = db.relationship('Prescription', backref='patient')
    hospitalizationrefer = db.relationship('Hospitalization', backref='patient')
    nursingrefer = db.relationship('Nursing', backref='patient')

class MedicalStaff(db.Model):  # 医生，管理员，院长一张表
    __tablename__ = 'medicalstaff'
    StaffID = db.Column(db.CHAR(4), primary_key=True)  # 每个用户记得添加用户组
    name = db.Column(db.CHAR(20))
    gender = db.Column(db.CHAR(1))
    department_ID = db.Column(db.CHAR(3), db.ForeignKey('department.departmentID'), nullable=True)
    entryDay = db.Column(db.DATE)
    retirementDate = db.Column(db.DATE)
    phoneNumber = db.Column(db.CHAR(11))
    officeNo = db.Column(db.CHAR(10))
    position = db.Column(db.CHAR(20))
    email = db.Column(db.CHAR(20))
    salary = db.Column(db.Integer)
    password = db.Column(db.VARCHAR(100))

    warehouserefer = db.relationship('Warehouse', backref='medicalstaff')
    reservationrefer = db.relationship('Reservation', backref='medicalstaff')
    hospitalizationrefer = db.relationship('Hospitalization', backref='medicalstaff')
    prescriptionrefer = db.relationship('Prescription', backref='medicalstaff')
    nursingrefer = db.relationship('Nursing', backref='medicalstaff')
    schedualrefer = db.relationship('Schedule', backref='medicalstaff')
#
class Department(db.Model):
    __tablename__ = 'department'
    departmentID=db.Column(db.CHAR(3), primary_key=True)
    departmentName = db.Column(db.CHAR(10))
    doctor_ID = db.Column(db.CHAR(4))
    nurse_ID = db.Column(db.CHAR(4))
    wardrefer = db.relationship('Ward', backref='department')


class Medicine(db.Model):
    __tablename__ = 'medicine'
    medicineID = db.Column(db.CHAR(3), primary_key=True)
    name = db.Column(db.CHAR(20))
    company = db.Column(db.CHAR(20))
    price = db.Column(db.Integer)
    warehouse_ID = db.Column(db.CHAR(2), db.ForeignKey("warehouse.warehouseID"))
    inDate = db.Column(db.DATE)
    expireDate = db.Column(db.DATE)
    stock = db.Column(db.Integer)
    description = db.Column(db.VARCHAR(100))

    prerefer = db.relationship('Prescription_Detail', backref='medicine')
#
#
#
#
class Warehouse(db.Model):
    __tablename__ = 'warehouse'
    warehouseID=db.Column(db.CHAR(2), primary_key=True)
    warehouseadmin_ID = db.Column(db.CHAR(4), db.ForeignKey("medicalstaff.StaffID"))
    medicinerefer = db.relationship('Medicine', backref='warehouse')

class Reservation(db.Model):
    __tablename__ = 'reservation'
    reservationID = db.Column(db.CHAR(4), primary_key=True)
    doctor_ID = db.Column(db.CHAR(4), db.ForeignKey("medicalstaff.StaffID"))
    patien_ID = db.Column(db.CHAR(4), db.ForeignKey("patient.patientID"))
    reservationDate = db.Column(db.DATE)
    description = db.Column(db.VARCHAR(100))

class Prescription(db.Model):
    __tablename__ = 'prescription'
    prescriptionID = db.Column(db.CHAR(5), primary_key=True)
    patien_ID = db.Column(db.CHAR(4), db.ForeignKey("medicalstaff.StaffID"))
    doctor_ID = db.Column(db.CHAR(4), db.ForeignKey("patient.patientID"))
    prescriptionDate = db.Column(db.DATE)
    paymentStatues = db.Column(db.CHAR(1))


class Prescription_Detail(db.Model):
    __tablename__ = 'prescription_detail'
    prescriptionID = db.Column(db.CHAR(5), primary_key=True)
    medicine_ID = db.Column(db.CHAR(3),  db.ForeignKey("medicine.medicineID"), primary_key=True)
    quantity = db.Column(db.Integer)


class Ward(db.Model):
    __tablename__ = 'ward'
    wardNo = db.Column(db.CHAR(4), primary_key=True, index=True)
    capacity = db.Column(db.Integer)
    department_ID = db.Column(db.CHAR(3), db.ForeignKey("department.departmentID"))
    bedrefer = db.relationship('Bed', backref='ward')

class Bed(db.Model):
    __tablename__ = 'bed'
    bedNo = db.Column(db.CHAR(4), primary_key=True)
    ward_No = db.Column(db.CHAR(4), db.ForeignKey("ward.wardNo"))
    price = db.Column(db.Integer)

    hospitalizationrefer = db.relationship('Hospitalization', backref='bed')

class Hospitalization(db.Model):
    __tablename__ = 'hospitalization'
    bedNo = db.Column(db.CHAR(4), db.ForeignKey("bed.bedNo"), primary_key=True)
    patient_ID = db.Column(db.CHAR(4), db.ForeignKey("patient.patientID"), primary_key=True)
    doctor_ID = db.Column(db.CHAR(4), db.ForeignKey("medicalstaff.StaffID"))
    nurse_ID = db.Column(db.CHAR(4))
    startDate = db.Column(db.DATE)
    endDate = db.Column(db.DATE)
    transferHospital = db.Column(db.CHAR(1))

class Nursing(db.Model):
    __tablename__ = 'nursing'
    patienID = db.Column(db.CHAR(4), db.ForeignKey("patient.patientID"), primary_key=True)
    nurseID = db.Column(db.CHAR(4), db.ForeignKey("medicalstaff.StaffID"), primary_key=True)
    date = db.Column(db.DATE)
    conditionDesc = db.Column(db.VARCHAR(200))

class Schedule(db.Model):
    __tablename__ = 'schedule'
    staff_ID = db.Column(db.CHAR(4), db.ForeignKey("medicalstaff.StaffID"), primary_key=True)
    date = db.Column(db.DATE, primary_key=True)
    timeInterval8 = db.Column(db.CHAR(1))
    timeInterval9 = db.Column(db.CHAR(1))
    timeInterval10 = db.Column(db.CHAR(1))
    timeInterval11 = db.Column(db.CHAR(1))
    timeInterval14 = db.Column(db.CHAR(1))
    timeInterval15 = db.Column(db.CHAR(1))
    timeInterval16 = db.Column(db.CHAR(1))
    timeInterval17 = db.Column(db.CHAR(1))

