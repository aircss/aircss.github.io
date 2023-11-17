Font family
###########


There are three defined classes that utilize attractive system fonts with appropriate
fallbacks for setting the typeface of a page or element. It is suggested that you
customize or extend this module to suit your own needs. However, relying on systems
fonts greatly improves page performance and can also help your web application/site
blend in with the user's operating system.


Mnemonics
=========

.. mnemonics:: air/src/typography/font-family.css


Examples
========

.. code:: html

    <h1 class="code">The quick brown fox ...<h1>

.. raw:: html

    <p class="code f-title fw7 lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
    </p>

.. code:: html

    <h1 class="serif">The quick brown fox ...<h1>

.. raw:: html

    <p class="serif f-title fw7 lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
    </p>

.. code:: html

    <h1 class="sans-serif">The quick brown fox ...<h1>

.. raw:: html

    <p class="sans-serif f-title fw7 lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
    </p>


Source code
===========

.. include:: ../../air/src/typography/font-family.css
    :code: css
    :start-after: */
