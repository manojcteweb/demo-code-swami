```python
class TimesheetTool:
    def __init__(self, hr_system, finance_system):
        self.hr_system = hr_system
        self.finance_system = finance_system

    def integrate_systems(self):
        try:
            self.hr_system.connect()
            self.finance_system.connect()
        except Exception as e:
            self.log_error("Integration error", e)

    def automate_approval(self, timesheet):
        try:
            if self.hr_system.approve_timesheet(timesheet):
                self.notify_user("Timesheet approved")
        except Exception as e:
            self.log_error("Approval error", e)

    def generate_invoice(self, timesheet):
        try:
            invoice = self.finance_system.create_invoice(timesheet)
            self.notify_user(f"Invoice generated: {invoice.id}")
        except Exception as e:
            self.log_error("Invoicing error", e)

    def automate_billing(self, invoice):
        try:
            self.finance_system.process_billing(invoice)
            self.notify_user(f"Billing processed for invoice: {invoice.id}")
        except Exception as e:
            self.log_error("Billing error", e)

    def provide_real_time_updates(self):
        try:
            updates = self.finance_system.get_updates()
            self.notify_user(f"Updates: {updates}")
        except Exception as e:
            self.log_error("Update error", e)

    def log_error(self, message, exception):
        print(f"{message}: {exception}")

    def notify_user(self, message):
        print(message)

# Example usage
hr_system = HRSystem()
finance_system = FinanceSystem()
tool = TimesheetTool(hr_system, finance_system)
tool.integrate_systems()
tool.automate_approval(timesheet)
tool.generate_invoice(timesheet)
tool.automate_billing(invoice)
tool.provide_real_time_updates()
```