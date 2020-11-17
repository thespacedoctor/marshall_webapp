{{ objname }} *(module)*
{{ underline }}===========



.. automodule:: {{ fullname }}


    {% block attributes %}
    {% if attributes %}
    .. rubric:: Properties

    .. autosummary::

        {% for item in attributes %}
          ~{{ item }}
        {%- endfor %}
        {% endif %}

    {% endblock %}


    {% block classes %}

    {% if classes %}
    .. rubric:: Classes

    .. autosummary::

        {% for item in classes %}
          ~{{ item }}
        {%- endfor %}
        {% endif %}

        {% endblock %}



    {% block functions %}


    {% if functions %}
    .. rubric:: Functions

    .. autosummary::

        {% for item in functions %}
          ~{{ item }}
        {%- endfor %}
        {% endif %}
        {% endblock %}


    
    
