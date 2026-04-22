/**
 * Results Header Component
 */
class ResultsHeaderController {
    public totalCount!: number;
    public currentPage!: number;
    public perPage!: number;
    public loading!: boolean;

    public getEndIndex(): number {
        return Math.min(this.currentPage * this.perPage, this.totalCount);
    }
}

const resultsHeader: ng.IComponentOptions = {
    bindings: {
        totalCount: '<',
        currentPage: '<',
        perPage: '=',
        onPerPageChange: '&',
        loading: '<'
    },
    templateUrl: 'src/templates/results-header.html',
    controller: ResultsHeaderController
};

angular.module('gleniganApp').component('resultsHeader', resultsHeader);
