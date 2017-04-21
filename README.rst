==========================
django CMS Accordion
==========================  

A plugin for django CMS which provides you an easy way to add accordion tabs to your pages. It's minimalistic and can be easily customized via CSS.

Installation
============

To get started using ``djangocms-simple-accordion``:

- install it with ``pip``::

    $ pip install djangocms-simple-accordion


- add the plugins to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'djangocms_accordion',
        ...
    )


- run ``migrate djangocms_accordion``.


Dependencies
=============
- Currently this plugin depends on bootstrap and glyphicons.


Customization
=============
You can just override some of the CSS rules. In order to find the correct one, nspect the generated HTML in the development tools in the browser of your choice.

However, here are some commonly used customization options to get you started:

**Tab-Icons**

.. code-block:: css

    .accordion-title .accordion-toggleIcon:after {
      font-size: 13px;
      content: '\e080';
    }
    .accordion-title.active .accordion-toggleIcon:after {
      content: '\e114';
    }

**Accordion Color**

.. code-block:: css

    .accordion {
      background-color: red;
    }

**Title font size**

.. code-block:: css

    .accordion-title {
      font-size: 20px;
    }

**Transition Time**

.. code-block:: css

    .u-accordion-transition {
      -webkit-transition: ease-in-out .2s;
      -moz-transition: ease-in-out .2s;
      -ms-transition: ease-in-out .2s;
      -o-transition: ease-in-out .2s;
      transition: ease-in-out .2s;
    }