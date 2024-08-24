#!/usr/bin/env python3.11
class Employee:
      def __init__(self,name,email_address,title,phone_number = None):
            self.name = name
            self.email_address = email_address
            self.title = title
            self.phone_number = phone_number
      
      def email_signature(self,include_phone=False):
            if include_phone and self.phone_number:
                  return f"{self.name} - {self.title}\n{self.email_address} ({self.phone_number})"
            else:
                  return f"{self.name} - {self.title}\n{self.email_address}"