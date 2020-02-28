{
gROOT->Reset();
TCanvas *cc = new TCanvas("cc","cc",0,0,500,500);
TLine *line = new TLine();
TArc *arc0 = new TArc();
arc0->DrawArc(.1,.1,.07);
TArc *arc1 = new TArc(.2,.2,.07);
arc1->Draw();
TArc *arc2 = new TArc(.3,.3,.07);
arc2->SetFillColor(kBlue);
arc2->Draw();
TArc *arc3 = new TArc(.2,.5,.2,45.,135.);
arc3->SetFillColor(kRed);
arc3->Draw();
line->DrawLine(.2,.5,.4,.7);
line->DrawLine(.2,.5,.0,.7);
TArc *arc4 = new TArc(.5,.5,.2,0,90.);
arc4->SetFillColor(kGreen);
arc4->Draw();
line->DrawLine(.5,.5,.7,.7);
line->DrawLine(.5,.5,.3,.7);
TArc *arc5 = new TArc(.8,.5,.2,180/4.,3.*180/4);
arc5->SetFillColor(kYellow);
arc5->Draw();
line->DrawLine(.8,.5,1.,.7);
line->DrawLine(.8,.5,.6,.7);
}
