# Copyright (c) 2022, Ami and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Registration(Document):
	def before_save(self):
          self.fullname = f'{self.firstname} {self.lastname or ""}'
