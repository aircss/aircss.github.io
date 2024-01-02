White space
###########

:icon: paragraph.svg
:summary: Sometime it is necessary to set a different strategy to handle white
    spaces and new lines from the default one web browser use in an element.


Sometime it is necessary to set a different strategy to handle white spaces and new
lines from the default one web browser use in an element.


Mnemonics
=========

.. mnemonics:: air/src/typography/white-space.css


Examples
========

*The borders of each container elements are visible to show the effects of the different
white-space attributes in the following examples.*


.. code:: html

    <p class="pre">Lorem ipsum ...</p>

.. raw:: html

    <p class="tl lh-body llm fw3 mb6 pre ba">
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
            tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
            At vero

                    eos et accusam et justo duo dolores et

                                                ea rebum. Stet clita kasd gubergren!

    </p>

.. code:: html

    <p class="nowrap">Lorem ipsum ...</p>

.. raw:: html

    <p class="lh-body llm fw3 pa3 mb6 nowrap ba">
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod sed diam voluptua.
    </p>

.. code:: html

    <p class="truncate">Lorem ipsum ...</p>

.. raw:: html

    <p class="tl lh-body llm fw3 pa3 mb6 truncate ba">
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
            tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
            At vero

                    eos et accusam et justo duo dolores et

                                                ea rebum. Stet clita kasd gubergren!

    </p>

Source code
===========

.. include:: ../../air/src/typography/white-space.css
    :code: css
    :start-after: */
