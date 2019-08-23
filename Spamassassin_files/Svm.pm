=head1 NAME

Mail::SpamAssassin::Plugin::Svm - determine spammishness using a Svm classifier

=head1 DESCRIPTION

This is a Support vector machien classifier which uses stemming and punctuation removal for
data cleaning,TFIDF for feature extarction, cross validation and grid search for parameter
tuning.

The results are incorporated into SpamAssassin as the BAYES_* rules.

=head1 METHODS

=cut

package Mail::SpamAssassin::Plugin::Svm;

use strict;
use warnings;
# use bytes;
use re 'taint';

use Digest::SHA qw(sha1 sha1_hex);

use Mail::SpamAssassin::Plugin;
use Mail::SpamAssassin::PerMsgStatus;
use Mail::SpamAssassin::Logger;

our @ISA = qw(Mail::SpamAssassin::Plugin);

sub new {
    my $class = shift;
    my ($main) = @_;

    $class = ref($class) || $class;
    my $self = $class->SUPER::new($main);
    bless ($self, $class);

    $self->{main} = $main;
    $self->{conf} = $main->{conf};
    $self->{use_ignores} = 1;

    $self->register_eval_rule("check_svm");
    return $self;
}

sub check_svm {
    my ($self, $pms, $fulltext) = @_;

    return 0 if (!$self->{conf}->{use_svm_learner});
    return 0 if (!$self->{conf}->{use_svm});

    if (!exists ($pms->{svm_score})) {
        my $timer = $self->{main}->time_method("check_svm");
        $pms->{svm_score} = $self->scan($pms, $pms->{msg});
    }

    if (defined $pms->{svm_score})
    {
        $pms->test_log(sprintf ("score: %3.4f", $pms->{svm_score}));
        return 1;
    }

    return 0;
}

sub scan{
    my ($self, $permsgstatus, $msg) = @_;
   
    #command to run the python script, msg will be passed as an
    #argument and the message status will be retuened as the output 
}

sub learn_svm{

    #Mbox file will be passed as an argument, formail will filter the headers
    #and the model will be trained.Values of the best_params will be returned
    #and a SVM classifier will be created which will handle the incoming 
    #mail.
}

1;




