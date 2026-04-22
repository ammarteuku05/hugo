/**
 * Filter Panel Component
 */
const filterPanel: ng.IComponentOptions = {
    bindings: {
        filters: '=',
        onFilterChange: '&',
        onReset: '&'
    },
    templateUrl: 'src/templates/filter-panel.html'
};

angular.module('gleniganApp').component('filterPanel', filterPanel);
