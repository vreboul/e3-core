from __future__ import annotations

import stevedore


def load_store(name, configuration, cache):
    plugin = stevedore.DriverManager("e3.store", name)

    return plugin.driver(configuration, cache)
