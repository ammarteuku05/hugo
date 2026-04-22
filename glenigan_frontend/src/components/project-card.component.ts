/**
 * Project Card Component
 */
const projectCard: ng.IComponentOptions = {
    bindings: {
        project: '<'
    },
    templateUrl: 'src/templates/project-card.html'
};

angular.module('gleniganApp').component('projectCard', projectCard);
