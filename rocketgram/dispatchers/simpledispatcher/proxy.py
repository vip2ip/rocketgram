# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


from .base import BaseSimpleDispatcher


class SimpleDispatcherProxy(BaseSimpleDispatcher):
    @property
    def inits(self):
        return self._init

    @property
    def shutdowns(self):
        return self._shutdown

    @property
    def handlers(self):
        return self._handlers

    @property
    def preprocessors(self):
        return self._preprocessors

    @property
    def postprocessors(self):
        return self._postprocessors