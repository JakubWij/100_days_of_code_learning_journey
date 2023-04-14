import smtplib
from flight_data import FlightData


class NotificationManager(FlightData):
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, mail, password, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection = None
        self.mail = mail
        self.password = password
    # def __init__(self, my_mail, password, flight):
    #     super().__init__(self.price, .......)# itd  w inicie odbieram klasę a w superze definiuję argumenty
    #     self.connection = None
    #     self.my_mail = my_mail
    #     self.password = password

    def send_mail(self):
        msg = f"Low price alert! Only £{self.price} to fly from {self.origin_city}-{self.origin_airport} to" \
              f" {self.destination_city}-{self.destination_airport}, from {self.out_date} to {self.return_date}\n\n"
        link = f"https://www.google.co.uk/flights?hl=en#flt={self.origin_airport}.{self.destination_airport}." \
               f"{self.out_date}*{self.destination_airport}.{self.origin_airport}.{self.return_date}"
        print(link)
        if self.stop_overs > 1:
            msg += f"Flight has {self.stop_overs} stop overs, via " \
                   f"{', '.join(self.via_city[:-1]) + ' and ' + self.via_city[-1]}."
        elif self.stop_overs > 0:
            msg += f"Flight has {int(self.stop_overs)} stop over, via {self.via_city[0]}."
        self.connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
        self.connection.starttls()
        self.connection.login(user=self.mail, password=self.password)
        self.connection.sendmail(from_addr=self.mail,
                                 to_addrs=self.mail,
                                 msg=msg.encode("utf-8"))

