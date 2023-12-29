Vertical align
##############

This module allows to set vertical alignment of an inline or inline-block box.


Mnemonics
=========

.. mnemonics:: air/src/layout/vertical-align.css


Examples
========

The following examples add visible top and botton borders on each element to
better show the different options available. 

.. code:: html

    <span>Reference</span>
    <span class="v-base">.v-base</span>
    <span class="v-top">.v-top</span>
    <span class="v-mid">.v-mid</span>
    <span class="v-btm">.v-btm</span>


.. raw:: html

    <div class="w-100 bb bt b--red mt5 mb4">
        <h1 class="dib mv5">Reference</h1>
        <h1 class="dib bb bt mv0 mh3 v-base">.v-base</h1>
        <h1 class="dib bb mv0 mh3 v-top">.v-top</h1>
        <h1 class="dib bb bt mv0 mh3 v-mid">.v-mid</h1>
        <h1 class="dib bt mv0 mh3 v-btm">.v-btm</h1>
    </div>



Source code
===========

.. include:: ../../air/src/layout/vertical-align.css
    :code: css
    :start-after: */
