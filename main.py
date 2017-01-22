#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():

    fortunes = [
    "You are a coding diety",
    "The world needs more people like you.",
    "Impress yourself.",
    "You will succeed at anything you do... so long as that thing is related to yarn or soap.",
    "You will receive a promotion soon."
    ]

    index = random.randint(0, 4)


    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_generator = 'Your fortune is: ' + fortune
        fortune_section = "<p>" + fortune_generator + "</p>"

        lucky_number = "<strong>" + str(random.randint(1, 100)) + "<strong>"
        number_generator = 'Your lucky number is: ' + lucky_number
        number_section = "<p>" + number_generator + "</p>"

        new_cookie_button = "<a href='.'><button>Give me another fortune cookie, please!</button></a>"

        content = header + fortune_section + number_section + new_cookie_button

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
