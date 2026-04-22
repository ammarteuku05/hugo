/**
 * Results Header Component
 */
const resultsHeader: ng.IComponentOptions = {
    bindings: {
        totalCount: '<',
        currentPage: '<',
        perPage: '=',
        onPerPageChange: '&',
        loading: '<'
    },
    templateUrl: 'src/templates/results-header.html',
    controller: function () {
        this.getEndIndex = () => {
            return Math.min(this.currentPage * this.perPage, this.totalCount);
        };
    }
};

angular.module('gleniganApp').component('resultsHeader', resultsHeader);
