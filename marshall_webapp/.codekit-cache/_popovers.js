! function($) {

    // "use strict"; // jshint ;_;

    /* POPOVER PUBLIC CLASS DEFINITION
     * =============================== */

    var Popover = function(element, options) {
        this.init('popover', element, options)
    }

    /* NOTE: POPOVER EXTENDS BOOTSTRAP-TOOLTIP.js
     ========================================== */

    Popover.prototype = $.extend({}, $.fn.tooltip.Constructor.prototype, {

        constructor: Popover

        ,
        setContent: function() {
            var $tip = this.tip(),
                title = this.getTitle(),
                content = this.getContent()

            $tip.find('.popover-title')[this.options.html ? 'html' : 'text'](title)
            $tip.find('.popover-content')[this.options.html ? 'html' : 'text'](content)

            $tip.removeClass('fade top bottom left right in')
        }

        ,
        hasContent: function() {
            return this.getTitle() || this.getContent()
        }

        ,
        getContent: function() {
            var content, $e = this.$element,
                o = this.options

            content = (typeof o.content == 'function' ? o.content.call($e[0]) : o.content) || $e.attr('data-content')

            return content
        }

        ,
        tip: function() {
            if (!this.$tip) {
                this.$tip = $(this.options.template)
            }
            return this.$tip
        }

        ,
        destroy: function() {
            this.hide().$element.off('.' + this.type).removeData(this.type)
        }

    })

    /* POPOVER PLUGIN DEFINITION
     * ======================= */

    var old = $.fn.popover

    $.fn.popover = function(option) {
        return this.each(function() {
            var $this = $(this),
                data = $this.data('popover'),
                options = typeof option == 'object' && option
            if (!data) $this.data('popover', (data = new Popover(this, options)))
            if (typeof option == 'string') data[option]()
        })
    }

    $.fn.popover.Constructor = Popover

    // added by dryx on November 7, 2014 -- make the popover persist when you enter it
    var originalLeave = $.fn.popover.Constructor.prototype.leave;
    $.fn.popover.Constructor.prototype.leave = function(e) {
        var container, self;
        self = $(e.currentTarget)[this.type](this._options).data(this.type);
        originalLeave.call(this, e);
        if (e.currentTarget) {
            container = $(".popover");
            return container.one("mouseenter", function() {
                clearTimeout(self.timeout);
                return container.one("mouseleave", function() {
                    return originalLeave.call(self, e);
                });
            });
        }
    };

    $.fn.popover.defaults = $.extend({}, $.fn.tooltip.defaults, {
        placement: 'right',
        trigger: 'click',
        content: '',
        template: '<div class="popover"><div class="arrow"></div><h3 class="popover-title"></h3><div class="popover-content"></div></div>'
    })

    /* POPOVER NO CONFLICT
     * =================== */

    $.fn.popover.noConflict = function() {
        $.fn.popover = old
        return this
    }

}(window.jQuery);

// opt into popovers
$("[rel='popover']").popover();
