Spacing
#######

Spacing allows to set the outer (margin) and inner (padding) space of an
element. The difference between margin and padding can have a huge impact on
the layout despite being invisible to the user.

Aircss spacing scale is based on the powers of two and provides eight steps.

Mnemonics
=========

.. raw:: html

    <div class="evenly-filled wrapped flex">
        <div class="pa2 w-100 w-25-m tc">
            <div class="db pa2 mb4 b bb noir-60">Bases</div>

            <span class="code red f7">p = padding</span><br>
            <span class="code red f7">m = margin</span><br>
            <span class="code red f7"></span><br>
        </div>


        <div class="pa2 w-100 w-50-m tc">
            <div class="db pa2 mb4 b bb noir-60">Modifiers</div>

            <div class="flex">
                <div class="flex column w-50 tl">
                    <div class="center">
                        <span class="red">a = all</span><br>
                        <br>
                    </div>
                    <div class="center">
                        <span class="red">v = vertical</span><br>
                        <span class="red">h = horizontal</span><br>
                        <br>
                    </div>
                    <div class="center">
                        <span class="red">t = top</span><br>
                        <span class="red">r = right</span><br>
                        <span class="red">b = bottom</span><br>
                        <span class="red">l = left</span><br>
                        <br>
                    </div>
                </div>

                <div class="flex column w-50 tl">
                    <div class="center">
                        <span class="red">0 = none</span><br>
                        <br>
                    </div>
                    <div class="center">
                        <span class="red">1 = 1st step in scale</span><br>
                        <span class="red">2 = 2nd step in scale</span><br>
                        <span class="red">3 = 3rd step in scale</span><br>
                        <span class="red">4 = 4th step in scale</span><br>
                        <span class="red">5 = 5th step in scale</span><br>
                        <span class="red">6 = 6th step in scale</span><br>
                        <span class="red">7 = 7th step in scale</span><br>
                        <span class="red">8 = 8th step in scale</span><br>
                    </div>
                </div>
            </div>

        </div>

        <div class="pa2 w-100 w-25-m tc">
            <div class="db pa2 mb4 b bb noir-60">Optional modifiers</div>

            <span class="red">-m  = medium</span><br>
            <span class="red">-l  = large</span><br>
        </div>
    </div>


Examples
========

It is possible to set the inner and outer spacing by choosing between ``.p*``
and ``.m*`` classes. However the following examples will only use outer spacing
to illustrate the features of this module.

The following example shows the eight steps of the scale in the case of an
horizontal margin.

.. raw:: html

    <div class="flex">
        <div class="wrapped flex bg--noir-40">
            <div class="w-100 ml0 pa2 pb3 bg--noir-10 b">left margin</div>

            <div class="w-100 ml0 pa2 bg--noir-10 code red">.ml0</div>
            <div class="w-100 ml1 pa2 bg--noir-10 code red">.ml1</div>
            <div class="w-100 ml2 pa2 bg--noir-10 code red">.ml2</div>
            <div class="w-100 ml3 pa2 bg--noir-10 code red">.ml3</div>
            <div class="w-100 ml4 pa2 bg--noir-10 code red">.ml4</div>
            <div class="w-100 ml5 pa2 bg--noir-10 code red">.ml5</div>
            <div class="w-100 ml6 pa2 bg--noir-10 code red">.ml6</div>
            <div class="w-100 ml7 pa2 bg--noir-10 code red">.ml7</div>
            <div class="w-100 ml8 pa2 bg--noir-10 code red">.ml8</div>
        </div>

        <div class="wrapped flex bg--noir-40">
            <div class="w-100 ml0 pa2 pb3 bg--noir-10 b tc">horizontal margin (left + right)</div>

            <div class="w-100 pa2 bg--noir-10 tc code red">.mh0</div>
            <div class="w-100 pa2 bg--noir-10 tc code red">.mh1</div>
            <div class="w-100 pa2 bg--noir-10 tc code red">.mh2</div>
            <div class="w-100 pa2 bg--noir-10 tc code red">.mh3</div>
            <div class="w-100 pa2 bg--noir-10 tc code red">.mh4</div>
            <div class="w-100 pa2 bg--noir-10 tc code red">.mh5</div>
            <div class="w-100 pa2 bg--noir-10 tc code red">.mh6</div>
            <div class="w-100 pa2 bg--noir-10 tc code red">.mh7</div>
            <div class="w-100 pa2 bg--noir-10 tc code red">.mh8</div>
        </div>


        <div class="wrapped flex bg--noir-40">
            <div class="w-100 ml0 pa2 pb3 bg--noir-10 b tr">right margin</div>

            <div class="w-100 mr0 pa2 bg--noir-10 tr code red">.ml0</div>
            <div class="w-100 mr1 pa2 bg--noir-10 tr code red">.ml1</div>
            <div class="w-100 mr2 pa2 bg--noir-10 tr code red">.ml2</div>
            <div class="w-100 mr3 pa2 bg--noir-10 tr code red">.ml3</div>
            <div class="w-100 mr4 pa2 bg--noir-10 tr code red">.ml4</div>
            <div class="w-100 mr5 pa2 bg--noir-10 tr code red">.ml5</div>
            <div class="w-100 mr6 pa2 bg--noir-10 tr code red">.ml6</div>
            <div class="w-100 mr7 pa2 bg--noir-10 tr code red">.ml7</div>
            <div class="w-100 mr8 pa2 bg--noir-10 tr code red">.ml8</div>
        </div>
    </div>

The choices of priority in aircss allow to define the space for multiple edges
at the same time and to override this rule with a more specific rule. As a
matter of fact, a rule for all four edges can be overriden by a rule for
vertical or horizontal edge and those latters overriden by an edge specific
rule (top, right, bottom and left).

.. code:: html

    <div class="mh5 ml8">...</div>

.. raw:: html

    <div class=" flex bg--noir-40">
        <div class="w-100 mh5 ml8 pa2 bg--noir-10 tc code red">.mh5 .ml8</div>
    </div>
