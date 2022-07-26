def main():
    from chainsaw import chainsaw_logger
    from chainsaw import powertimer
    from time import sleep

    @powertimer
    def test():
        chainsaw_logger.info("This is info")
        chainsaw_logger.debug("This is debugging")
        chainsaw_logger.warning("This is a warning")
        chainsaw_logger.error("This is an error")
        sleep(1)
    
    test()

if __name__=='__main__':
    main()