import os

def main():
    mode = os.getenv('MODE', 'sandbox')
    print(f"Trading bot running in {mode} mode")
    # TODO: Implement trading logic

if __name__ == '__main__':
    main()
