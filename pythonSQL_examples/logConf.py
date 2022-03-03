import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style= '{',
    filename= 'mylog.log',
    filemode= 'w'
)