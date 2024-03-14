#importing libraries
import sys


#defining a funtion that will return our custom exception
def custom_error_msg_exception(error,error_details:sys):
    _,_,tb=error_details.exc_info()
    filename=tb.tb_frame.f_code.co_filename
    error_msg=f"Error has occured in the {filename} and line number is {tb.tb_lineno} and error is {error}"
    return error_msg


#define the exception class
class credits_exception(Exception):
    def __init__(self,error_msg,error_details) -> None:
        super().__init__(error_msg)
        self.error_msg=custom_error_msg_exception(error_msg,error_details)

    def __str__(self):
        return self.error_msg







