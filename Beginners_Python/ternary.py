#condition_if_true if condition else condition_if_else

IS_FRIEND = True
CAN_MESSAGE = "message allowed" if IS_FRIEND else "not allowed to message"
print(CAN_MESSAGE)