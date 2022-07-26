def main():
    from chainsaw import Logger
    from chainsaw import benchmark
    from time import sleep

    @benchmark
    def test():
        print(Logger.logger)
        Logger.logger.info("This is info")
        Logger.logger.debug("This is debugging")
        Logger.logger.warning("This is a warning")
        Logger.logger.error("This is an error")
        sleep(1)
    
    test()

if __name__=='__main__':
    main()