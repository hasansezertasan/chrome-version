"""Allow ``python -m chrome_version`` to invoke the CLI entrypoint."""
# Copyright (c) 2023 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Licensed under the MIT License

from chrome_version.cli import main

if __name__ == "__main__":
    main()
