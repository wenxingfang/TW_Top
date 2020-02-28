//#include "Math/DistFunc.h"
{
TF1 *f = new TF1("f","ROOT::Math::chisquared_pdf(x,[0])",0,200);
f->SetParameter(0,93);  // set the n.d.f to 2
f->Draw();
}
